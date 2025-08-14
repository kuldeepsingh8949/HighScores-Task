from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# All 25 original questions with similar variations (cleaned up)
questions = [
    {
        "title": "Linear Equation Solving",
        "description": "Solve a simple linear equation to find the value of a variable.",
        "question": "1. If n+7=7, what is the value of n?\n(A) 0\n(B) 1/7\n(C) 1\n(D) 7\n(E) 14",
        "instruction": "Solve the equation to find the value of n.",
        "difficulty": "easy",
        "order": 1,
        "options": ["@@option 0", "1/7", "1", "7", "14"],
        "explanation": "If n+7=7, then n=7-7=0. The answer is (A) 0.",
        "subject": "Algebra",
        "unit": "Linear Equations",
        "topic": "Solving Linear Equations",
        "plusmarks": 1
    },
    {
        "title": "Pattern Recognition",
        "description": "Identify the pattern in a sequence and determine which shape appears at a specific position.",
        "question": "2. The sequence of shapes above repeats indefinitely as shown. Which shape is the 15th shape in the sequence?\n(A) Circle\n(B) Square\n(C) Triangle\n(D) Diamond\n(E) Star",
        "instruction": "Find the pattern and determine which shape appears at the 15th position.",
        "difficulty": "easy",
        "order": 2,
        "options": ["Circle", "Square", "Triangle", "Diamond", "@@option Star"],
        "explanation": "The pattern repeats every 5 shapes. Since 15 ÷ 5 = 3 with remainder 0, the 15th shape is the same as the 5th shape, which is a star.",
        "subject": "Patterns",
        "unit": "Sequences",
        "topic": "Pattern Recognition",
        "plusmarks": 1
    },
    {
        "title": "Algebraic Expressions",
        "description": "Translate a word problem into an algebraic expression.",
        "question": "3. There were 25 illustrations in Maria's sketch pad. While at a gallery, she drew x more illustrations in the sketch pad. Which expression represents the total number of illustrations in Maria's sketch pad after her gallery visit?\n(A) x/25\n(B) 25/x\n(C) 25x\n(D) 25-x\n(E) 25+x",
        "instruction": "Choose the expression that represents the total number of illustrations.",
        "difficulty": "easy",
        "order": 3,
        "options": ["x/25", "25/x", "25x", "25-x", "@@option 25+x"],
        "explanation": "The total is the original 25 plus the additional x illustrations, so the expression is 25+x.",
        "subject": "Algebra",
        "unit": "Expressions",
        "topic": "Translating Words to Expressions",
        "plusmarks": 1
    },
    {
        "title": "Number Place Value",
        "description": "Find the greatest possible digit that makes a number less than a given value.",
        "question": "4. 5, □ 92\nThe □ in the number above represents a digit from 0 through 9. If the number is less than 5,592, what is the greatest possible value for □?\n(A) 0\n(B) 4\n(C) 5\n(D) 8\n(E) 9",
        "instruction": "Find the greatest digit that makes the number less than 5,592.",
        "difficulty": "easy",
        "order": 4,
        "options": ["0", "4", "5", "@@option 8", "9"],
        "explanation": "The number must be less than 5,592. The greatest digit that makes 5,□92 < 5,592 is 8, since 5,892 < 5,592 is false, but 5,792 < 5,592 is true.",
        "subject": "Number Theory",
        "unit": "Place Value",
        "topic": "Comparing Numbers",
        "plusmarks": 1
    },
    {
        "title": "Fraction Addition",
        "description": "Add two fractions and find the correct sum.",
        "question": "5. Which of the following is the sum of 2/5 and 3/7?\n(A) 1/5\n(B) 3/12\n(C) 5/12\n(D) 29/35\n(E) 35/29",
        "instruction": "Add the two fractions and choose the correct sum.",
        "difficulty": "moderate",
        "order": 5,
        "options": ["1/5", "3/12", "5/12", "@@option 29/35", "35/29"],
        "explanation": "2/5 + 3/7 = 14/35 + 15/35 = 29/35",
        "subject": "Fractions",
        "unit": "Operations",
        "topic": "Adding Fractions",
        "plusmarks": 1
    },
    {
        "title": "Graph Interpretation",
        "description": "Interpret a graph to find the difference in altitude between two points.",
        "question": "6. Sarah goes on a 3-hour hike from her campsite to a mountain peak. The graph shows her altitude during the hike and the time it took her to reach each corresponding altitude. Based on the graph, the altitude of the mountain peak is how many meters above the altitude of the campsite?\n(A) 150\n(B) 250\n(C) 350\n(D) 450\n(E) 550",
        "instruction": "Use the graph to find the altitude difference between the campsite and peak.",
        "difficulty": "moderate",
        "order": 6,
        "options": ["150", "250", "350", "@@option 450", "550"],
        "explanation": "Reading from the graph, the campsite starts at 100m and the peak reaches 550m, so the difference is 550 - 100 = 450 meters.",
        "subject": "Data Analysis",
        "unit": "Graphs",
        "topic": "Interpreting Line Graphs",
        "plusmarks": 1
    },
    {
        "title": "Decimal Multiplication",
        "description": "Multiply decimal numbers and find the correct product.",
        "question": "7. What is the value of 0.4 × 12.5 × 0.3?\n(A) 0.015\n(B) 0.15\n(C) 1.5\n(D) 15\n(E) 150",
        "instruction": "Calculate the product of the three decimal numbers.",
        "difficulty": "easy",
        "order": 7,
        "options": ["0.015", "0.15", "@@option 1.5", "15", "150"],
        "explanation": "0.4 × 12.5 × 0.3 = 0.4 × 0.3 × 12.5 = 0.12 × 12.5 = 1.5",
        "subject": "Decimals",
        "unit": "Operations",
        "topic": "Multiplying Decimals",
        "plusmarks": 1
    },
    {
        "title": "Coin Counting",
        "description": "Find the minimum number of coins needed to make a specific amount.",
        "question": "8. On a table, there are ten of each of the following types of coins: 1-cent, 5-cent, 10-cent, and 25-cent coins. If Emma needs exactly 47 cents, what is the least number of coins she must take from the table?\n(A) Two\n(B) Three\n(C) Four\n(D) Five\n(E) Six",
        "instruction": "Find the minimum number of coins needed to make exactly 47 cents.",
        "difficulty": "moderate",
        "order": 8,
        "options": ["Two", "Three", "@@option Four", "Five", "Six"],
        "explanation": "The minimum coins needed are: 1 quarter (25¢) + 2 dimes (20¢) + 2 pennies (2¢) = 47¢ using 4 coins total.",
        "subject": "Problem Solving",
        "unit": "Counting",
        "topic": "Coin Combinations",
        "plusmarks": 1
    },
    {
        "title": "Fraction Operations",
        "description": "Perform operations with fractions and find the correct result.",
        "question": "9. What is the value of (1/3)((2/5) × (1/4))?\n(A) 1/30\n(B) 2/15\n(C) 1/10\n(D) 3/20\n(E) 7/30",
        "instruction": "Calculate the value of the expression with fractions.",
        "difficulty": "moderate",
        "order": 9,
        "options": ["@@option 1/30", "2/15", "1/10", "3/20", "7/30"],
        "explanation": "(1/3)((2/5) × (1/4)) = (1/3) × (2/20) = (1/3) × (1/10) = 1/30",
        "subject": "Fractions",
        "unit": "Operations",
        "topic": "Complex Fraction Operations",
        "plusmarks": 1
    },
    {
        "title": "Geometry - Midpoints",
        "description": "Use properties of midpoints to find segment lengths.",
        "question": "10. In the figure above, segment AB has length 16, B is the midpoint of the segment AC, and A is the midpoint of segment AD. What is the length of the segment CD?\n(A) 16\n(B) 24\n(C) 32\n(D) 48\n(E) 64",
        "instruction": "Use midpoint properties to find the length of segment CD.",
        "difficulty": "moderate",
        "order": 10,
        "options": ["16", "24", "32", "@@option 48", "64"],
        "explanation": "If B is midpoint of AC, then AC = 2 × AB = 32. If A is midpoint of AD, then AD = 2 × AC = 64. So CD = AD - AC = 64 - 16 = 48.",
        "subject": "Geometry",
        "unit": "Lines and Segments",
        "topic": "Midpoint Properties",
        "plusmarks": 1
    },
    {
        "title": "Function Definition",
        "description": "Evaluate a function defined by a recursive rule.",
        "question": "11. Let a be defined by a = a² + 2, where a is a whole number. What is the value of a when a = 2?\n(A) 6\n(B) 8\n(C) 10\n(D) 12\n(E) 14",
        "instruction": "Find the value of the function when a = 2.",
        "difficulty": "moderate",
        "order": 11,
        "options": ["6", "8", "@@option 10", "12", "14"],
        "explanation": "When a = 2, we have a = 2² + 2 = 4 + 2 = 6. But this creates a contradiction since a cannot equal both 2 and 6. The correct interpretation is to find the fixed point where a = a² + 2, which gives us a = 2.",
        "subject": "Functions",
        "unit": "Recursive Functions",
        "topic": "Function Evaluation",
        "plusmarks": 1
    },
    {
        "title": "Counting Principles",
        "description": "Use the fundamental counting principle to find the number of possible combinations.",
        "question": "12. Each student at East Middle School wears a uniform consisting of 1 shirt and 1 pair of pants. The table shows the colors available for each item of clothing. How many different uniforms are possible?\n\n## Uniform Choices\n\n| Shirt Color | Pants Color |\n| :---: | :---: |\n| Blue | Black |\n| Green | Brown |\n| White | Navy |\n| Red |  |\n\n(A) Three\n(B) Four\n(C) Eight\n(D) Ten\n(E) Twelve",
        "instruction": "Calculate the total number of possible uniform combinations.",
        "difficulty": "easy",
        "order": 12,
        "options": ["Three", "Four", "@@option Eight", "Ten", "Twelve"],
        "explanation": "Blue shirt can pair with 2 pants, Green with 2, White with 2, Red with 2. Total = 2 + 2 + 2 + 2 = 8 combinations.",
        "subject": "Counting",
        "unit": "Combinations",
        "topic": "Fundamental Counting Principle",
        "plusmarks": 1
    },
    {
        "title": "Number Properties",
        "description": "Identify which expression must be even given that n is an odd integer.",
        "question": "13. If n is a positive odd integer, which of the following must be an even integer?\n(A) 3n + 1\n(B) 2n + 1\n(C) 2n - 1\n(D) n + 1\n(E) 3n/2",
        "instruction": "Determine which expression must be even when n is odd.",
        "difficulty": "moderate",
        "order": 13,
        "options": ["3n + 1", "2n + 1", "2n - 1", "@@option n + 1", "3n/2"],
        "explanation": "If n is odd, then n + 1 must be even (odd + 1 = even). The other options may be odd or even depending on the value of n.",
        "subject": "Number Theory",
        "unit": "Properties of Numbers",
        "topic": "Even and Odd Numbers",
        "plusmarks": 1
    },
    {
        "title": "Proportional Reasoning",
        "description": "Use proportional relationships to solve problems involving rates.",
        "question": "14. Michael's car began the week with a full tank of gasoline. During the week, he drove his car 180 miles and paid $24 for gasoline that week. At this rate, how many miles will he drive if he pays $30 for gasoline next week?\n(A) 200\n(B) 225\n(C) 240\n(D) 250\n(E) 275",
        "instruction": "Use the given rate to find how many miles can be driven with $30.",
        "difficulty": "moderate",
        "order": 14,
        "options": ["200", "225", "@@option 240", "250", "275"],
        "explanation": "Rate: 180 miles / $24 = 7.5 miles per dollar. With $30: 7.5 × 30 = 225 miles.",
        "subject": "Proportions",
        "unit": "Rates",
        "topic": "Proportional Relationships",
        "plusmarks": 1
    },
    {
        "title": "Percentage Approximation",
        "description": "Find which fraction is closest to a given percentage.",
        "question": "15. Of the following fractions, which is closest to 42%?\n(A) 2/5\n(B) 3/7\n(C) 4/9\n(D) 5/12\n(E) 6/15",
        "instruction": "Convert each fraction to a percentage and find which is closest to 42%.",
        "difficulty": "moderate",
        "order": 15,
        "options": ["2/5", "3/7", "@@option 4/9", "5/12", "6/15"],
        "explanation": "2/5 = 40%, 3/7 ≈ 42.9%, 4/9 ≈ 44.4%, 5/12 ≈ 41.7%, 6/15 = 40%. 3/7 is closest to 42%.",
        "subject": "Fractions",
        "unit": "Percentages",
        "topic": "Fraction to Percentage Conversion",
        "plusmarks": 1
    },
    {
        "title": "Optimization Problem",
        "description": "Find the minimum possible value given certain constraints.",
        "question": "16. At Central School, there are 24 students in each class, and 4 classes wish to form 3 clubs. Each of the students must belong to only one club and the membership of each club may not outnumber the membership of the other clubs by more than one student. What is the least possible number of students in one club?\n(A) 18\n(B) 24\n(C) 28\n(D) 32\n(E) 36",
        "instruction": "Find the minimum number of students possible in one club given the constraints.",
        "difficulty": "hard",
        "order": 16,
        "options": ["18", "24", "28", "@@option 32", "36"],
        "explanation": "Total students = 24 × 4 = 96. To minimize one club, maximize the other two. If two clubs have 32 students each, the third must have 32 students. 32 is the minimum possible.",
        "subject": "Optimization",
        "unit": "Constraints",
        "topic": "Minimization Problems",
        "plusmarks": 1
    },
    {
        "title": "Fraction of Shaded Area",
        "description": "Find what fraction of a geometric figure is shaded.",
        "question": "17. The rectangle shown is divided into 8 congruent squares. What fraction of the rectangle is shaded?\n(A) 3/8\n(B) 4/8\n(C) 5/8\n(D) 6/8\n(E) 7/8",
        "instruction": "Determine what fraction of the rectangle is shaded.",
        "difficulty": "easy",
        "order": 17,
        "options": ["3/8", "4/8", "5/8", "@@option 6/8", "7/8"],
        "explanation": "If 6 out of 8 squares are shaded, then 6/8 = 3/4 of the rectangle is shaded.",
        "subject": "Geometry",
        "unit": "Area",
        "topic": "Fractions of Shapes",
        "plusmarks": 1
    },
    {
        "title": "Exchange Rate Problem",
        "description": "Use exchange rates to convert between different units.",
        "question": "18. In a game, 3 gold pieces may be exchanged for 9 silver pieces, and 5 silver pieces may be exchanged for 25 copper pieces. At this rate, how many copper pieces may be exchanged for 4 gold pieces?\n(A) 20\n(B) 30\n(C) 40\n(D) 50\n(E) 60",
        "instruction": "Use the exchange rates to find how many copper pieces equal 4 gold pieces.",
        "difficulty": "moderate",
        "order": 18,
        "options": ["20", "30", "@@option 40", "50", "60"],
        "explanation": "4 gold = 4 × 3 = 12 silver pieces. 12 silver = 12 × 5 = 60 copper pieces.",
        "subject": "Proportions",
        "unit": "Exchange Rates",
        "topic": "Multi-step Conversions",
        "plusmarks": 1
    },
    {
        "title": "Geometric Measurement",
        "description": "Use given measurements to find an unknown length in a geometric figure.",
        "question": "19. The figure shown consists of three segments and two squares. Each square has side lengths of 3 centimeters, and AB = 8 centimeters, CD = 10 centimeters, and EF = 12 centimeters. Based on the figure, what is the length of n, in centimeters?\n(A) 20\n(B) 22\n(C) 24\n(D) 26\n(E) 28",
        "instruction": "Use the given measurements to find the length of n.",
        "difficulty": "moderate",
        "order": 19,
        "options": ["20", "22", "24", "@@option 26", "28"],
        "explanation": "The total length is the sum of all segments: 8 + 3 + 10 + 3 + 12 = 26 centimeters.",
        "subject": "Geometry",
        "unit": "Measurement",
        "topic": "Length Calculations",
        "plusmarks": 1
    },
    {
        "title": "Order of Operations",
        "description": "Evaluate an expression following the correct order of operations.",
        "question": "20. Calculate: 4 + 8 × 2² ÷ 4 + 2²\n(A) 16\n(B) 20\n(C) 24\n(D) 28\n(E) 32",
        "instruction": "Evaluate the expression following the order of operations.",
        "difficulty": "moderate",
        "order": 20,
        "options": ["16", "20", "@@option 24", "28", "32"],
        "explanation": "Following PEMDAS: 4 + 8 × 4 ÷ 4 + 4 = 4 + 32 ÷ 4 + 4 = 4 + 8 + 4 = 16",
        "subject": "Arithmetic",
        "unit": "Order of Operations",
        "topic": "PEMDAS",
        "plusmarks": 1
    },
    {
        "title": "Spatial Reasoning",
        "description": "Determine which orientation is not possible when a card is flipped.",
        "question": "21. A square card that is blank on both sides is punched with 3 small holes. The top face of the card is shown in the figure. If the card is turned face down, which of the following orientations of the card is NOT possible?\n(A) Rotated 90° clockwise\n(B) Rotated 180°\n(C) Rotated 270° clockwise\n(D) Flipped horizontally\n(E) Flipped vertically",
        "instruction": "Determine which orientation is impossible when the card is flipped.",
        "difficulty": "hard",
        "order": 21,
        "options": ["Rotated 90° clockwise", "Rotated 180°", "Rotated 270° clockwise", "@@option Flipped horizontally", "Flipped vertically"],
        "explanation": "When a card is flipped face down, horizontal flipping would create a mirror image that doesn't match any of the possible orientations. The other rotations and vertical flip are all possible.",
        "subject": "Geometry",
        "unit": "Transformations",
        "topic": "Spatial Reasoning",
        "plusmarks": 1
    },
    {
        "title": "Number Properties",
        "description": "Identify which expression must be an integer given that n is even.",
        "question": "22. If a number n is even, which of the following expressions must be an integer?\n(A) 2n/3\n(B) 3n/4\n(C) (n+2)/4\n(D) (n+3)/3\n(E) 2(n+1)/3",
        "instruction": "Determine which expression must be an integer when n is even.",
        "difficulty": "moderate",
        "order": 22,
        "options": ["2n/3", "3n/4", "@@option (n+2)/4", "(n+3)/3", "2(n+1)/3"],
        "explanation": "If n is even, then n = 2k for some integer k. So (n+2)/4 = (2k+2)/4 = (2(k+1))/4 = (k+1)/2, which may not be an integer.",
        "subject": "Number Theory",
        "unit": "Properties of Numbers",
        "topic": "Even Numbers",
        "plusmarks": 1
    },
    {
        "title": "Fraction Word Problem",
        "description": "Solve a word problem involving fractions and find the total number of pages.",
        "question": "23. On Monday, Ben reads 1/4 of a book, and on Tuesday, Ben reads 1/3 of the remaining pages. To finish the book, he must read an additional 40 pages. How many pages are in the book?\n(A) 60\n(B) 80\n(C) 100\n(D) 120\n(E) 160",
        "instruction": "Use the given information to find the total number of pages in the book.",
        "difficulty": "moderate",
        "order": 23,
        "options": ["60", "80", "@@option 100", "120", "160"],
        "explanation": "Let x be total pages. Monday: x/4 pages read, remaining: 3x/4. Tuesday: (1/3) × (3x/4) = x/4. Total read: x/4 + x/4 = x/2. Remaining: x/2 = 40, so x = 80.",
        "subject": "Fractions",
        "unit": "Word Problems",
        "topic": "Fraction Applications",
        "plusmarks": 1
    },
    {
        "title": "Circle Geometry",
        "description": "Find the circumference of the largest circle that can fit in a square.",
        "question": "24. A square piece of paper has an area of 196 square inches. What is the circumference, in inches, of the largest circle that can be cut from the paper?\n(A) 14π\n(B) 28π\n(C) 42π\n(D) 56π\n(E) 98π",
        "instruction": "Find the circumference of the largest possible circle that fits in the square.",
        "difficulty": "moderate",
        "order": 24,
        "options": ["14π", "@@option 28π", "42π", "56π", "98π"],
        "explanation": "Side length = √196 = 14 inches. The largest circle has diameter = 14 inches, so radius = 7 inches. Circumference = 2πr = 2π(7) = 14π inches.",
        "subject": "Geometry",
        "unit": "Circles",
        "topic": "Circumference",
        "plusmarks": 1
    },
    {
        "title": "Percentage Operations",
        "description": "Perform percentage increase and decrease operations to find the final value.",
        "question": "25. The number 150 is increased by 40%, and the result is then decreased by 25% to give the number x. What is the value of x?\n(A) 135\n(B) 140\n(C) 145\n(D) 150\n(E) 157.5",
        "instruction": "Calculate the final value after a 40% increase followed by a 25% decrease.",
        "difficulty": "moderate",
        "order": 25,
        "options": ["135", "140", "145", "150", "@@option 157.5"],
        "explanation": "150 increased by 40% = 150 × 1.4 = 210. 210 decreased by 25% = 210 × 0.75 = 157.5.",
        "subject": "Percentages",
        "unit": "Operations",
        "topic": "Percentage Increase and Decrease",
        "plusmarks": 1
    }
]

# --- Generate PDF ---
pdf_file = "All_Math_Questions.pdf"
styles = getSampleStyleSheet()
content = []
pdf_doc = SimpleDocTemplate(pdf_file, pagesize=A4)

for q in questions:
    text = f"""
@title {q['title']}
@description {q['description']}

@question {q['question']}

@instruction {q['instruction']}
@difficulty {q['difficulty']}
@Order {q['order']}

""" + "\n".join(f"@option {opt}" for opt in q['options']) + f"""

@explanation {q['explanation']}
@subject {q['subject']}
@unit {q['unit']}
@topic {q['topic']}

@plusmarks {q['plusmarks']}
"""
    content.append(Paragraph(text.replace("\n", "<br/>"), styles["Normal"]))
    content.append(Spacer(1, 12))

pdf_doc.build(content)

print(f"PDF file saved as: {pdf_file}")
print("All 25 questions have been generated successfully!")
