import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

class Chatbot:
    def __init__(self, model_name="Qwen/Qwen2.5-1.5B-Instruct", use_gpu=False):
        self.model_name = model_name
        self.use_gpu = use_gpu
        self.device = "cuda" if use_gpu else "cpu"
        self.model = None
        self.tokenizer = None
        
        self._load_model()

    def _load_model(self):
        if self.use_gpu:
            nf4_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                quantization_config=nf4_config,
                device_map="auto",
                low_cpu_mem_usage=True
            )
        else:
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                device_map="cpu",
                torch_dtype=torch.float32,
                low_cpu_mem_usage=True
            )
            
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, return_token_type_ids=False)

    def generate_response(self, chat_history, temperature=0.7, max_tokens=512):
        
        # 1. Prompt template
        text = self.tokenizer.apply_chat_template(
            chat_history, 
            tokenize=False, 
            add_generation_prompt=True
        )
        
        # 2. Tokenize
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)

        # 3. Generate
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )

        # 4. Decode
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        return response