string studentName = "Sophia Johnson";
string course1Name = "English 101";
string course2Name = "Algebra 101";
string course3Name = "Biology 101";
string course4Name = "Computer Science I";
string course5Name = "Psychology 101";

int course1Credit = 3;
int course2Credit = 3;
int course3Credit = 4;
int course4Credit = 4;
int course5Credit = 3;

int gradeA = 4;
int gradeB = 3;

int course1Grade = gradeA;
int course2Grade = gradeB;
int course3Grade = gradeB;
int course4Grade = gradeB;
int course5Grade = gradeA;

int totalCreditHour = 0;
totalCreditHour += course1Credit;
totalCreditHour += course2Credit;
totalCreditHour += course3Credit;
totalCreditHour += course4Credit;
totalCreditHour += course5Credit;

int totalGradePointer =0;
totalGradePointer += course1Credit * course1Grade;
totalGradePointer += course2Credit * course2Grade;
totalGradePointer += course3Credit * course3Grade;
totalGradePointer += course4Credit * course4Grade;
totalGradePointer += course5Credit * course5Grade;

decimal gradePointerAverage = (decimal)totalGradePointer / totalCreditHour;
Console.WriteLine($"Grade Pointer Average: {gradePointerAverage:F2}");
int leadingDegit = (int)gradePointerAverage;
int firstDigit = (int)(gradePointerAverage *10) %10;
int secondDigit = (int)(gradePointerAverage *100) %10;
int thirdDigit = (int)(gradePointerAverage *1000) %10;

Console.WriteLine($"course1Name:  {course1Name}, {course1Credit},{course1Grade}");
Console.WriteLine($"course2Name:  {course2Name}, {course2Credit},{course2Grade}");
Console.WriteLine($"course3Name:  {course3Name}, {course3Credit},{course3Grade}");
Console.WriteLine($"course4Name:  {course4Name}, {course4Credit},{course4Grade}");
Console.WriteLine($"course5Name:  {course5Name}, {course5Credit},{course5Grade}");
Console.WriteLine($"Final GPA is: {leadingDegit}.{firstDigit}{secondDigit}{thirdDigit}");

Console.WriteLine($"course1Name:  {course1Name}\t\t{course1Credit}\t\t{course1Grade}");
Console.WriteLine($"course2Name:  {course2Name}\t\t{course2Credit}\t\t{course2Grade}");
Console.WriteLine($"course3Name:  {course3Name}\t\t{course3Credit}\t\t{course3Grade}");
Console.WriteLine($"course4Name:  {course4Name}\t{course4Credit}\t\t{course4Grade}");
Console.WriteLine($"course5Name:  {course5Name}\t\t{course5Credit}\t\t{course5Grade}");
Console.WriteLine($"\nFinal GPA: \t\t\t\t{leadingDegit}.{firstDigit}{secondDigit}{thirdDigit}");

