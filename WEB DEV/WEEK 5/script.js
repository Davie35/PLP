// ===========================
// ❤️ Part 1: JavaScript Basics
// ===========================
document.getElementById("checkAgeBtn").addEventListener("click", function() {
  let age = prompt("Enter your age:");
  if (age >= 18) {
    document.getElementById("ageResult").textContent = "You are an adult!";
  } else {
    document.getElementById("ageResult").textContent = "You are a minor!";
  }
});

// ===========================
// ❤️ Part 2: Functions
// ===========================

// Function 1: Sum two numbers
function sumNumbers(a, b) {
  return a + b;
}
document.getElementById("sumBtn").addEventListener("click", function() {
  let result = sumNumbers(5, 7);
  document.getElementById("sumResult").textContent = "The sum is: " + result;
});

// Function 2: Toggle visibility of text
function toggleVisibility() {
  const msg = document.getElementById("toggleMessage");
  if (msg.style.display === "none") {
    msg.style.display = "block";
  } else {
    msg.style.display = "none";
  }
}
document.getElementById("toggleBtn").addEventListener("click", toggleVisibility);

// ===========================
// 🔁 Part 3: Loops
// ===========================

// Example 1: Countdown using for loop
document.getElementById("countdownBtn").addEventListener("click", function() {
  let output = "";
  for (let i = 5; i >= 1; i--) {
    output += i + "... ";
  }
  document.getElementById("countdownResult").textContent = output + "Go!";
});

// Example 2: Loop through array
const fruits = ["Apple", "Banana", "Mango", "Orange"];
document.getElementById("listBtn").addEventListener("click", function() {
  const fruitList = document.getElementById("fruitList");
  fruitList.innerHTML = ""; // clear old list
  fruits.forEach(fruit => {
    const li = document.createElement("li");
    li.textContent = fruit;
    fruitList.appendChild(li);
  });
});

// ===========================
// 🌐 Part 4: DOM Manipulation
// ===========================

// Example 1: Change text
document.getElementById("changeTextBtn").addEventListener("click", function() {
  document.getElementById("textTarget").textContent = "Text has been changed!";
});

// Example 2: Add new list item
document.getElementById("addItemBtn").addEventListener("click", function() {
  const li = document.createElement("li");
  li.textContent = "New Item " + (document.querySelectorAll("#itemList li").length + 1);
  document.getElementById("itemList").appendChild(li);
});

// Example 3: Toggle background color
document.getElementById("colorBtn").addEventListener("click", function() {
  document.body.classList.toggle("bg-toggled");
});
