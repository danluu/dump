// Open csv

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>


int main() {
    // Parse poll_answers.txt (csv). Format is:
    // user,question,is_male,is_white,answer.
    // We ignore is_male and is_white (for now?)

    // Question ids run from 1 to 27. We'll shift it down to use 0 to 26 and store them in a u_int32.
    // We set a bit to 1 if answer is 1, otherwise it's 0.
    // We should check for and discard any incompletes.

    // User ids run from 50 to 62654.

    #define MIN_USER 50
    #define MAX_USER 62654
    
    std::fstream infile("poll_answers.txt");

    std::string line;

    std::vector<int> num_answers(MAX_USER, 0);
    std::vector<uint32_t> answers(MAX_USER, 0);

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        std::string s_user, s_question, s_is_male, s_is_white, s_answer;

        std::getline(iss, s_user, ',');
        std::getline(iss, s_question, ',');
        std::getline(iss, s_is_male, ',');
        std::getline(iss, s_is_white, ',');
        std::getline(iss, s_answer, ',');

        // std::cout << "string verison " << s_user << "," << s_answer << std::endl;

        uint32_t user = std::stoul(s_user);
        uint32_t question = std::stoul(s_question) - 1;
        uint32_t answer = std::stoul(s_answer);


        // std::cout << "uint version " << user << "," << question << "," << answer << std::endl;

        // die early
        if (user != 50) {
           // break;
        }

        ++num_answers[user];
        if (answer == 1) {
            // std::cout << "saw 1" << std::endl;
            answers[user] |= 1 << question;
        }

       //  std::cout << "vec " << answers[user] << std::endl;
    }

    std::unordered_map<int, int> num_answers_histogram;
    for (const auto &count : num_answers) {
        ++num_answers_histogram[count];
    }

    for (const auto& [kk,vv]: num_answers_histogram) {
        std::cout << kk << "," << vv << std::endl;
    }

    return 0;
}