//
// Created by Golfer on 2020/7/24.
//

#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

// DFS Version
class Solution {
public:
    map<Node*, Node*> visited;
    Node* cloneGraph(Node* node) {
        Node node_clone = Node(node->val);
        Node* node_clone_pointer = &node_clone;
        visited[node] = node_clone_pointer;
        for (Node* & neighbor : node->neighbors) {
//            node_clone_pointer->neighbors.resize(node_clone_pointer->neighbors.size() + 1);
            if (visited.find(neighbor) == visited.end()) {
                Node* neighbor_clone = cloneGraph(neighbor);
//                node_clone_pointer->neighbors[node_clone_pointer->neighbors.size() - 1] = neighbor_clone;
                node_clone_pointer->neighbors.push_back(neighbor_clone);
            } else{
//                node_clone_pointer->neighbors[node_clone_pointer->neighbors.size() - 1] = visited[neighbor];
                node_clone_pointer->neighbors.push_back(visited[neighbor]);
            }
        }
        return node_clone_pointer;
    }
};

int main() {
    vector<vector<int>> graph = {{2, 4}, {1, 3}, {2, 4}, {1, 3}};
    map<int, Node*> node_map;
    for (int i = 1; i <= graph.size(); i++) {
        if (node_map.find(i) == node_map.end()) {
            Node node = Node(i);
            Node* node_p = &node;
            node_map[i] = node_p;
        }
        for (int j = 0; j < graph[i-1].size(); j++) {
            if (node_map.find(graph[i][j]) == node_map.end()) {
                Node node_neighbor = Node(graph[i][j]);
                Node* node_p_neighbor = &node_neighbor;
                node_map[graph[i][j]] = node_p_neighbor;
                node_map[i]->neighbors.push_back(node_map[graph[i][j]]);
            }
            else {
                node_map[i]->neighbors.push_back(node_map[graph[i][j]]);
            }
        }
    }

    Solution solution = Solution();
    Node* clone_graph = solution.cloneGraph(node_map[0]);

    return 0;
}
