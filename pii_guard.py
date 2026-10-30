import logging
logging.getLogger("presidio-analyzer").setLevel(logging.ERROR)

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

print("Loading AI Models...\n")
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()



local_phone_pattern = Pattern(name="local_phone_pattern", regex=r"\b\d{3}-\d{4}\b", score=0.8)
phone_recognizer = PatternRecognizer(supported_entity="PHONE_NUMBER", patterns=[local_phone_pattern])
analyzer.registry.add_recognizer(phone_recognizer)


name_recognizer = PatternRecognizer(supported_entity="PERSON", deny_list=["Ananda"])
analyzer.registry.add_recognizer(name_recognizer)



def protect_pii(text):
    print(f"--- Original Input ---")
    print(text)
  
    results = analyzer.analyze(
        text=text,
        language='en',
        entities=["EMAIL_ADDRESS", "PHONE_NUMBER", "PERSON", "CREDIT_CARD"]
    )
    
    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )
    
    print(f"--- Safe Output (Redacted) ---")
    print(anonymized_result.text)
    print("-" * 40 + "\n")




protect_pii("Hi, my name is Ananda and my email is ananda@example.com.")
protect_pii("Please charge my card: 4111 1111 1111 1111.")
protect_pii("Call me at 555-0199 if you need anything.")
