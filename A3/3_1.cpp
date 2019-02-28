#include <iostream>
#include <queue>
#include <string>
#include <vector>

const int capacity[] = {4,3};

int* enc1(int current[2]) {
    if(current[0] < capacity[0]) {
        int* ret = new int[2];
        ret[0] = capacity[0];
        ret[1] = current[1];
        return ret;
    } else {
        return NULL;
    }
}

int* enc2(int current[2]) {
    if(current[1] < capacity[1]) {
        int* ret = new int[2];
        ret[0] = current[0];
        ret[1] = capacity[1];
        return ret;
    } else {
        return NULL;
    }
}

int* esv1(int current[2]) {
    if(current[0] > 0) {
        int* ret = new int[2];
        ret[0] = 0;
        ret[1] = current[1];
        return ret;
    } else {
        return NULL;
    }
}

int* esv2(int current[2]) {
    if(current[1] > 0) {
        int* ret = new int[2];
        ret[0] = current[0];
        ret[1] = 0;
        return ret;
    } else {
        return NULL;
    }
}

int* d12(int current[2]) {
    if((current[0] > 0) && (current[1] < capacity[1])) {
        if(current[0] >= capacity[1] - current[1]) {
            int* ret = new int[2];
            ret[0] = current[0] - (capacity[1] - current[1]);
            ret[1] = capacity[1];
            return ret;
        } else {
            int* ret = new int[2];
            ret[0] = 0;
            ret[1] = current[1] + current[0];
            return ret;
        }
    } else {
        return NULL;
    }
}

int* d21(int current[2]) {
    if((current[1] > 0) && (current[0] < capacity[0])) {
        if(current[1] >= capacity[0] - current[0]) {
            int* ret = new int[2];
            ret[0] = capacity[0];
            ret[1] = current[1] - (capacity[0] - current[0]);
            return ret;
        } else {
            int* ret = new int[2];
            ret[0] = current[0] + current[1];
            ret[1] = 0;
            return ret;
        }
    } else {
        return NULL;
    }
}

typedef struct Node {
    int* current;
    std::vector<std::string> path;
    int value;
} Node;

void print(Node n) {
    for(std::string p : n.path) {
        std::cout << p << std::endl;
    }
    //std::cout << n.current[0] << "  -   " << n.current[1] << std::endl; 
}

// bool operator<(const Node& a, const Node& b) {
//   return a.value <= b.value;
// }

bool operator==(const Node& a, const Node& b) {
  return a.current[0] == b.current[0] && a.current[1] == b.current[1];
}

int main(int argc, char const *argv[]){

    const int estado_obj[] = {1,0};

    std::priority_queue<Node> q;
    //std::vector<Node> aux = {};

    Node start;
    start.current = new int[2];
    start.current[0] = 0; start.current[1] = 0;
    start.path = {};
    start.value = 0;

    q.push(start);

    typedef int* (*fn)(int[2]);
    std::vector<fn> operators = {enc1, enc2, esv1, esv2, d12, d21};

    while(true) {    
        Node top = q.top();

        if(top.current[0] == estado_obj[0] && top.current[1] == estado_obj[1]) break;
        q.pop();
        aux.push_back(top);

        for(int i = 0; i < operators.size(); i++) {
            auto res = operators[i](top.current);
            if(!res) continue;
            Node n;
            n.current = res;
            n.path = top.path;
            n.path.push_back(std::to_string(i));
            n.value = 1;

            q.push(n);
        } 
        // std::cin.get();
        delete top.current;
        q.pop();
    }

    print(q.top());

    return 0;
}
