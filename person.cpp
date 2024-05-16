#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades(); 
		int fib();	
	private:
		int age;
		int fib_help(int); 
	};

Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){ 
	return age/10.0; 
	}

int Person::fib_help(int n){ 
	if (n <= 1){
		return n;
	} else{
		return fib_help(n-1) + fib_help(n-2);
	}
	}

int Person::fib(){ //Added fib	
	return fib_help(age);
	}


extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();} //Added double
	int Person_fib(Person* person) {return person->fib();} 		//Added fib

	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}