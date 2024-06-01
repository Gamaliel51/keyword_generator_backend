from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("Voicelab/vlt5-base-keywords")
tokenizer = T5Tokenizer.from_pretrained("Voicelab/vlt5-base-keywords", legacy=False)


def get_keywords(input_string):
    task_prefix = "Keywords: "
    input_sequences = [task_prefix + input_string]
    input_ids = tokenizer(
        input_sequences, return_tensors="pt", truncation=True, max_length=512
    ).input_ids
    output = model.generate(input_ids, no_repeat_ngram_size=10
                            , num_beams=4, max_length=1000, min_length=20, num_return_sequences=1, early_stopping=True)
    predicted = tokenizer.decode(output[0], skip_special_tokens=True)
    return predicted
