#include <iostream>
#include <queue>
#include <string>
#include <vector>

bool DEPTH = false;

const std::pair<int, int> capacity = std::make_pair(4,3);

// ------ OPERATORS --------

bool enc1(std::pair<int, int> current, std::pair<int, int>& ret) {
    if(current.first < capacity.first) {
        ret = std::make_pair(capacity.first,current.second);
        return true;
    } else {
        return false;
    }
}

bool enc2(std::pair<int, int> current, std::pair<int, int>& ret) {
    if(current.second < capacity.second) {
        ret = std::make_pair(current.first, capacity.second);
        return true;
    } else {
        return false;
    }
}

bool esv1(std::pair<int, int> current, std::pair<int, int>& ret) {
    if(current.first > 0) {
        ret = std::make_pair(0, current.second);
        return true;
    } else {
        return false;
    }
}

bool esv2(std::pair<int, int> current, std::pair<int, int>& ret) {
    if(current.second > 0) {
        ret = std::make_pair(current.first, 0);
        return true;
    } else {
        return false;
    }
}

bool d12(std::pair<int, int> current, std::pair<int, int>& ret) {
    if((current.first > 0) && (current.second < capacity.second)) {
        if(current.first >= capacity.second - current.second) {
            ret = std::make_pair(current.first - (capacity.second - current.second),
                                capacity.second);
            return true;
        } else {
            ret = std::make_pair(0, current.second + current.first);
            return true;
        }
    } else {
        return false;
    }
}

bool d21(std::pair<int, int> current, std::pair<int, int>& ret) {
    if((current.second > 0) && (current.first < capacity.first)) {
        if(current.second >= capacity.first - current.first) {
            ret = std::make_pair(capacity.first,
                                current.second - (capacity.first - current.first));
            return true;
        } else {
            ret = std::make_pair(current.first + current.second, 0);
            return true;
        }
    } else {
        return false;
    }
}

std::string operators_name(int index) {
    switch (index)
    {
        case 0:
            return "enc1";
        case 1:
            return "enc2";
        case 2:
            return "esv1";
        case 3:
            return "esv2";
        case 4:
            return "d12";
        case 5:
            return "d21";
        default:
            return "";
    }
}


// ------- NODE ----------


typedef struct Node {
    std::pair<int, int> current;
    std::vector<std::string> path;
    std::pair<int, int> parent;
    int value;
} Node;

void print(Node n) {
    for(std::string p : n.path) {
        std::cout << p << std::endl;
    }
}

bool operator<(const Node& a, const Node& b) {
    if(DEPTH)
        return a.value <= b.value;
    else
        return a.value < b.value;
}

// -----------------------

int main(int argc, char const *argv[]){
    if(argc < 3 || argc > 4) {
        std::cout << "Usage: " << argv[0] << " <final state 1> <final state 2> (-1 for unspecified) [depth]"<< std::endl;
        return -1;
    }
    
    if(argc == 4) DEPTH = (strcmp(argv[3], "true") == 0) ? true : false;

    const std::pair<int, int> estado_obj = std::make_pair(atoi(argv[1]), atoi(argv[2]));

    std::priority_queue<Node> q;

    Node start;
    start.current = std::make_pair(0, 0);
    start.path = {};
    start.parent = std::make_pair(0, 0);
    start.value = 0;

    q.push(start);

    typedef bool (*fn)(std::pair<int, int>, std::pair<int, int>&);
    std::vector<fn> operators = {enc1, enc2, esv1, esv2, d12, d21};

    while(true) {    
        Node top = q.top();  
        print(top); std::cout << std::endl;      

        if(((estado_obj.first  == -1) ? true : top.current.first  == estado_obj.first) &&
           ((estado_obj.second == -1) ? true : top.current.second == estado_obj.second)) break;

        q.pop();

        std::pair<int, int> updated;
        for(int i = 0; i < operators.size(); i++) {
            bool res = operators[i](top.current, updated);

            if(!res ||
            (updated.first == top.parent.first &&
            updated.second == top.parent.second)) continue;

            Node n;
            n.current = updated;
            n.path = top.path;
            n.path.push_back(operators_name(i));
            n.value = 1;
            n.parent = top.current;

            q.push(n);
        } 
    }

    print(q.top());

    return 0;
}
