using System;

namespace Studentteacher_OOP
{

    public class Campusmember
    {
        public string name = "";
        public string sex = "";
        public int age = 0;

        public Campusmember(string p_name, string p_sex, int p_age)
        {
            name = p_name;
            sex = p_sex;
            age = p_age;
        }
    }

    class Teacher : Campusmember
    {
        int teacher_id = 0;

        public Teacher(string p_name, string p_sex, int p_age, int p_teacher_id) : base(p_name, p_sex, p_age)
        {
            teacher_id = p_teacher_id;
        }

        
    }

    class Student : Campusmember
    {
        int student_id = 0;

        public Student(string p_name, string p_sex, int p_age, int p_student_id) : base(p_name, p_sex, p_age)
        {
            student_id = p_student_id;
        }

        
    }

    class Program
    {
        static void Main(string[] args)
        {
            Student a = new Student("Alfred Linkler", "Male", 21, 2432);

            Console.WriteLine(a.age);
            Console.ReadLine();
        }
    }
}
