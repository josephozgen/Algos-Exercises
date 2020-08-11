const myObj = {
    data: 'abc',
    loggerA: () => {
        console.log(this.data)
    },
    loggerB() {
        console.log(this.data);
    },
};

myObj.loggerA();
myObj.loggerB();