#include <iostream>
#include <string>

class Entity {
    private:
        const char* name;
        mutable int querys;
    public:
        Entity(const char* name) : name(name) {querys++;}
        const char* GetName() const { return name;}
};

int main() {
    Entity e0 = Entity("Misael");

    std::cout << e0.GetName() << std::endl;
}