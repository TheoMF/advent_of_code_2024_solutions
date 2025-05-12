#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <boost/algorithm/string/regex.hpp>

int main(int argc, char *argv[]) {
    // initialize variables
    std::vector<int> data_left_list, data_right_list;
    std::string file_line;
    std::vector<std::string> splitted_line_vec;
    int result_part1 = 0;
    int result_part2 = 0;
    std::ifstream file("../input_data.txt");

    // fill input data inside two int vector
    while (std::getline (file, file_line)) {
        boost::algorithm::split_regex(splitted_line_vec, file_line, boost::regex("   "));
        data_left_list.push_back(std::stoi(splitted_line_vec[0]));
        data_right_list.push_back(std::stoi(splitted_line_vec[1]));
    }
    file.close();

    //sort the two lists by ascending order
    std::sort(data_left_list.begin(),data_left_list.end());
    std::sort(data_right_list.begin(),data_right_list.end());

    //compute the results for the two parts of the puzzle and print it
    for (int idx =0; idx<data_left_list.size();idx++){
        result_part1 += std::abs(data_right_list[idx] - data_left_list[idx]);
        result_part2 += data_left_list[idx]*std::count(data_right_list.begin(),data_right_list.end(), data_left_list[idx]);
    }
    std::cout<< "result part1 "<< result_part1<<std::endl;
    std::cout<< "result part2 "<< result_part2<<std::endl;
    
    return 0;

}