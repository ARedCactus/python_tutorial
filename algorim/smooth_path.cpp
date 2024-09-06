#include <vector>
#include <iostream>
#include <algorithm>

struct point{
    double x_;
    double y_;

    point(double x, double y)
    : x_(x), y_(y){}

    double& operator[](int index){
        return index==0? x_ : y_;
    }

    friend std::ostream& operator<<(std::ostream &out, point p){
        out << p.x_ << " " << p.y_;
        return out;
    }
};

std::vector<point> vec_origin_{{0, 0}, {0, 1}, {0, 2},
    {1, 2}, {2, 2}, {3, 2}, {4, 2}, {4, 3}, {4, 4}};

void smoothPath(std::vector<point> &vec_origin, std::vector<point> &vec_after,
    double weight_data=0.5, double weight_smooth=0.1, double tolerance=0.000001){
    vec_after = vec_origin;
    double change{tolerance};
    while(change >= tolerance){
        change = 0;
        for(int i{1}; i < vec_origin.size()-1; ++i){
            for(int j{0}; j < 2; ++j){
                auto d1 = weight_data * (vec_origin[i][j] - vec_after[i][j]);
                auto d2 = 
                    weight_smooth * (vec_after[i-1][j] + vec_after[i+1][j] - 2*vec_after[i][j]);
                change += std::abs(d1 + d2);
                vec_after[i][j] += d1+d2;
            }
        }
    }
}

int main(){
    std::vector<point> vec_after_;
    smoothPath(vec_origin_, vec_after_);
    std::vector<point> vec_2{{2, 2}};
    vec_after_ = vec_2;
    std::for_each(vec_after_.begin(), vec_after_.end(), [](point p){
        std::cout << p << "\n";
    });
    
    return 0;
}