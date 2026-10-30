# SWYNEX-Model-or-API-Integration
Task 2: Prototype for PII Guard using Microsoft Presidio AI model for text redaction.

##  Custom AI Enhancements
The default Microsoft Presidio model sometimes struggles with regional names (like Indian names) and local phone number formats (without country codes). 

To solve this, I built **Custom Recognizers**:
1. A Regex pattern to catch local phone numbers (e.g., 555-0199).
2. A DenyList rule to guarantee specific regional names are caught.

This proves that the AI model can be customized and improved for specific user contexts.


# SWYNEX – Model or API Integration

## Task 2: PII Guard Prototype

A prototype for detecting and redacting Personally Identifiable Information (PII) using the **Microsoft Presidio AI framework**.

## 🧠 Custom AI Enhancements

The default Microsoft Presidio model sometimes struggles to recognize regional names (such as Indian names) and local phone number formats (especially those without country codes).

To address these limitations, I implemented **Custom Recognizers**:

1. **Regex Pattern:** Detects local phone number formats (e.g., `555-0199`).
2. **DenyList Recognizer:** Ensures specific regional names are identified and flagged for redaction.

These enhancements demonstrate how the Presidio framework can be customized and improved to handle region-specific PII detection requirements.

## 🚀 How to Run This Prototype

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

Clone this repository or download the project files.

### 2. Install Dependencies

Install the required Python libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Download the English Language Model

Install the spaCy English language model required by Presidio:

```bash
python -m spacy download en_core_web_lg
```

### 4. Run the Prototype

Execute the Python script:

```bash
python pii_guard.py
```

---

**Technologies Used:** Python · Microsoft Presidio · spaCy · Regular Expressions (Regex)
