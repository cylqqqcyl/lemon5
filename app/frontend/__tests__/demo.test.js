function demo(a, b) {
    return a + b;
  }
  
// module.exports = demo;  // Export the function as 'demo' in the src folder


// const demo = require('./demo');  // Import the function as 'demo' in the test folder

test('adds 1 + 2 to equal 3', () => {
  expect(demo(1, 2)).toBe(3);  // Use 'demo' instead of 'sum'
});
