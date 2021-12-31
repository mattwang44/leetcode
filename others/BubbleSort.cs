using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BUBBLESORT
{
   
    class Program
    {
        static void BubbleSort(int[] intArray)
        {
            int temp = 0;
            bool swapped;
            for (int i = 0; i < intArray.Length; i++)
            {
                swapped = false;
                for (int j = 0; j < intArray.Length - 1 - i; j++)
                    if (intArray[j] > intArray[j + 1])
                    {
                        temp = intArray[j];
                        intArray[j] = intArray[j + 1];
                        intArray[j + 1] = temp;
                        if (!swapped)
                            swapped = true;
                    }
                if (!swapped)
                    return;
            }
        }

        static void Main(string[] args)
        {
            Console.Write("Please input numbers: \n");
            string input_str;
            input_str = Console.ReadLine();

            Console.WriteLine("-----After Sorting-----");

            string[] input_str_arr = input_str.Split(' ');
            int input_len = input_str_arr.Length;
            int[] input_int_arr = Array.ConvertAll(input_str_arr, s => int.Parse(s));

            // example of parsing string of one number
            // int x = Int32.Parse(TextBoxD1.Text);  

            // Sorting Algorithms
            BubbleSort(input_int_arr);
            for (int i = 0; i < input_len; i++)
            {
                Console.Write(input_int_arr[i] + " ");
            }
                       
            Console.ReadLine();
        }
    }
}
