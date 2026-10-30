# SWYNEX-Model-or-API-Integration
Task 2: Prototype for PII Guard using Microsoft Presidio AI model for text redaction.

##  Custom AI Enhancements
The default Microsoft Presidio model sometimes struggles with regional names (like Indian names) and local phone number formats (without country codes). 

To solve this, I built **Custom Recognizers**:
1. A Regex pattern to catch local phone numbers (e.g., 555-0199).
2. A DenyList rule to guarantee specific regional names are caught.

This proves that the AI model can be customized and improved for specific user contexts.
