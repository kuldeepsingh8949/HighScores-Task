# Math Question Generator

This project uses Python to generate **Word** and **PDF** files containing multiple-choice math questions in a structured format.  
The generated questions are inspired by base problems but adapted to new contexts while preserving the underlying math concepts.

## 📂 Project Files

### Core Scripts
- `generate_questions.py` → Original script that generates 2 sample questions in both `.docx` and `.pdf` formats.
- `all_math_questions.py` → Comprehensive script with 25 math questions (includes LaTeX formatting).
- `pdf_only_questions.py` → Clean version that generates only PDF with 25 simplified math questions.
- `simple_math_questions.py` → Minimal template file.

### Output Files
- `Generated_Math_Questions.docx` → Original Word file with 2 sample questions.
- `Generated_Math_Questions.pdf` → Original PDF file with 2 sample questions.
- `All_Math_Questions.pdf` → Complete PDF with all 25 math questions.
- `README.md` → This file.

## 📜 Generated Questions

### Original Sample Questions (2)
1. **Pizza Topping Choices** - A combinatorics problem about calculating the total number of possible pizzas based on crust and topping options.
2. **Golf Ball Packaging** - A geometry problem about calculating the dimensions of a rectangular box containing tightly packed golf balls.

### Complete Set of 25 Math Questions
The project now includes a comprehensive set of 25 similar math questions covering various topics:

#### Algebra & Expressions
- Linear equation solving
- Algebraic expressions from word problems
- Function evaluation

#### Geometry & Measurement
- Pattern recognition
- Midpoint properties
- Area and fractions of shapes
- Circle geometry and circumference
- Spatial reasoning

#### Fractions & Operations
- Fraction addition and operations
- Complex fraction calculations
- Fraction word problems
- Percentage approximations

#### Number Theory & Properties
- Place value and number comparison
- Even/odd number properties
- Order of operations

#### Problem Solving & Applications
- Graph interpretation
- Decimal operations
- Coin counting problems
- Proportional reasoning
- Exchange rate problems
- Optimization problems

## 🔧 Question Output Format

All questions follow this structured format:
```
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
```

## 📦 Install Dependencies

```bash
pip install python-docx reportlab
```

## ▶️ How to Run This Project

### Prerequisites
Make sure you have Python installed on your system. This project works with Python 3.6+.

### Step 1: Install Dependencies
First, install the required Python packages:

```bash
pip install python-docx reportlab
```

### Step 2: Choose Your Script

#### Option A: Generate 2 Sample Questions (Word + PDF)
```bash
python generate_questions.py
```
**Output**: Creates `Generated_Math_Questions.docx` and `Generated_Math_Questions.pdf`

#### Option B: Generate All 25 Questions (PDF Only)
```bash
python questions25.py
```
**Output**: Creates `All_Math_Questions.pdf` with comprehensive question set

### Step 3: Check Generated Files
After running either script, you'll find the generated files in your project directory:
- **Word documents**: `.docx` files
- **PDF files**: `.pdf` files

### Step 4: View Results
- **Word files**: Open with Microsoft Word, LibreOffice Writer, or any compatible word processor
- **PDF files**: Open with any PDF viewer (Adobe Reader, Chrome, Firefox, etc.)

### Troubleshooting
- **Import Error**: Make sure you've installed dependencies with `pip install python-docx reportlab`
- **Permission Error**: Ensure you have write permissions in the project directory
- **File Not Found**: Check that you're running the script from the project root directory

## 🎯 Features

- **25 Similar Math Questions**: Each question is a variation of the original, maintaining mathematical concepts while changing context and numbers
- **Multiple Output Formats**: Support for both Word (.docx) and PDF (.pdf) generation
- **Structured Format**: Consistent tagging system for easy parsing and organization
- **Difficulty Levels**: Questions categorized as easy, moderate, or hard
- **Comprehensive Coverage**: Topics span algebra, geometry, fractions, number theory, and problem solving
- **Answer Key**: Correct answers marked with `@@option` for easy identification
- **Detailed Explanations**: Step-by-step solutions for each question

## 📚 Question Categories

- **Easy**: Basic operations, simple equations, fundamental concepts
- **Moderate**: Multi-step problems, fraction operations, geometric reasoning
- **Hard**: Optimization problems, spatial reasoning, complex constraints
