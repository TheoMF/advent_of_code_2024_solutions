#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
#include <boost/algorithm/string/regex.hpp>

/**
 * Test if string is a number or contains one, returns it's size.
 */
int get_number_from_string(std::string str){
    for (int number_digits=4;number_digits>0;number_digits--){
        std::string substring = str.substr(0,number_digits);
        if (std::all_of(substring.begin(), substring.end(), ::isdigit)){
            if (number_digits==4){
                // number has too many digits
                return 0;
            }
            return number_digits;
        }
    }
    return 0;
}

/**
 * Return multiplication result if substring format is valid, 0 otherwise.
 */
int get_result_from_substring(std::string substring){
    // test we have the first parenthesis
    if (substring[0] != '('){
        return 0;
    }

    // test we have the first number
    int number_size=get_number_from_string(substring.substr(1,4));
    if (number_size == 0){
        return 0;
    }
    int first_number = std::stoi(substring.substr(1,number_size));
    
    // test comma is here
    int comma_idx = 1+ number_size;
    if (substring[comma_idx] != ','){
        return 0;
    }
        
    // test we have the second number
    number_size=get_number_from_string(substring.substr(comma_idx+1,4));
    if (number_size == 0){
        return 0;
    }
    int second_number = std::stoi(substring.substr(comma_idx+1,number_size));

    // test we have the last parenthesis
    int parenthesis_idx =comma_idx + 1 + number_size;
    if (substring[parenthesis_idx] != ')'){
        return 0;
    }

    //return value
    return first_number * second_number;
}

int main(int argc, char *argv[]) {
    // initialize variables
    std::string file_line,substring;
    std::vector<std::string> splitted_line_vec;
    int result_part1 = 0;
    int result_part2 = 0;
    int do_idx = 0;
    int dont_idx = 0;
    bool mul_enabled = true;
    std::ifstream file("../input_data.txt");

    while (std::getline (file, file_line)) {
        // split the input string with "mul" so that we only have to parse (number1,number2) afterwards
        boost::algorithm::split_regex(splitted_line_vec, file_line, boost::regex("mul"));

        for (int idx=1;idx<splitted_line_vec.size();idx++){
            //get multiplication result from substring for each part of the puzzle
            substring = splitted_line_vec[idx];
            result_part1 += get_result_from_substring(substring);
            if (mul_enabled){
                result_part2+=get_result_from_substring(substring);
            }

            // update mul_enabled variable for the second part of the puzzle
            do_idx = 0;
            dont_idx = 0;
            if (substring.find("do()") != std::string::npos){
                do_idx = substring.find("do()");
                mul_enabled = true;
            }
            if (substring.find("don't()") != std::string::npos){
                dont_idx = substring.find("don't()");
                if (dont_idx > do_idx){
                    mul_enabled = false;
                }
            }
        }
    }
    file.close();
    std::cout << "result part1 "<< result_part1<<std::endl;
    std::cout << "result part2 "<< result_part2<<std::endl;
    
    return 0;
}