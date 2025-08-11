# Math Question Generator

This project uses Python to generate **Word** and **PDF** files containing multiple-choice math questions in a structured format.  
The generated questions are inspired by base problems but adapted to new contexts while preserving the underlying math concepts.

## 📂 Project Files
- `generate_questions.py` → Python script that generates the questions in both `.docx` and `.pdf` formats.
- `Generated_Math_Questions.docx` → Output Word file containing the generated questions.
- `Generated_Math_Questions.pdf` → Output PDF file containing the generated questions.
- `README.md` → This file.

## 📜 Generated Questions
### 1. Pizza Topping Choices
A combinatorics problem about calculating the total number of possible pizzas based on crust and topping options.

### 2. Golf Ball Packaging
A geometry problem about calculating the dimensions of a rectangular box containing tightly packed golf balls.

Both follow the **Question Output Format**:
@title Question title
@description Short description of the problem
@question Full question text with tables/images if applicable
@instruction Instruction for the student
@difficulty easy/moderate/hard
@Order Question number
@option Option text
@@option Correct option text
@explanation Explanation of the correct answer
@subject Curriculum subject
@unit Curriculum unit
@topic Curriculum topic
@plusmarks Marks for correct answer



Install Dependencies
pip install python-docx reportlab


▶️ Usage
Run the script:
python generate_questions.py
