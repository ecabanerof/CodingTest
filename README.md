# CodingTest

# Coding Challenges Repository

Welcome to the Coding Challenges Repository! This project contains solutions for two fascinating problems:

1. **Encrypted Sum Number:** A challenge where you repeatedly sum adjacent digits in a list and form a final encrypted number.
2. **Maximum Score with k-Consistency:** A problem where you maximize the contiguous days with the same stock price after removing up to `k` elements.

---

## Problem 1: Encrypted Sum Number

### Challenge Description

Complete the `findNumber` function. The function is expected to return a **STRING** and accepts an **INTEGER_ARRAY numbers** as its parameter.

### Explanation

- **Start** with a list of digits.
- **Add** each pair of neighboring digits.
- **Take only the last digit** (mod 10) of each sum and form a new list.
- **Repeat** the process until only two digits remain.
- Those two digits form the final encrypted number.

### Example

Given the list: `[1, 2, 3, 4, 5]`

1. **Iteration 1:**
   - 1 + 2 = 3  
   - 2 + 3 = 5  
   - 3 + 4 = 7  
   - 4 + 5 = 9  
   - **New list:** `[3, 5, 7, 9]`

2. **Iteration 2:**
   - 3 + 5 = 8  
   - 5 + 7 = 12 → 2 (last digit)  
   - 7 + 9 = 16 → 6 (last digit)  
   - **New list:** `[8, 2, 6]`

3. **Iteration 3:**
   - 8 + 2 = 10 → 0 (last digit)  
   - 2 + 6 = 8  
   - **New list:** `[0, 8]`

4. **Final Output:** `"08"`

---

## Problem 2: Maximum Score with k-Consistency

### Challenge Description

Complete the `findMaximumScore` function. The function is expected to return an **INTEGER** and accepts the following parameters:
- **INTEGER_ARRAY stockPrices**: an array of stock prices.
- **INTEGER k**: the maximum number of elements that can be removed.

### Explanation

1. **Sliding Window Approach:**
   - **Unique Value Iteration:**  
     The function iterates over each unique value in the `stockPrices` array. For each unique value, it attempts to find the maximum number of contiguous days where the stock return equals this value after removing up to `k` other elements.
  
2. **Window Maintenance:**
   - **Pointers:**  
     `left` and `right` pointers define the current window.
   - **Counters:**
     - `removals`: Counts the number of elements in the current window that do not match the `unique_value`.
     - `count_same`: Counts the number of elements in the current window that match the `unique_value`.
  
3. **Expanding the Window:**
   - For each `right` index, if the current element matches the `unique_value`, increment `count_same`. Otherwise, increment `removals`.
  
4. **Shrinking the Window:**
   - If `removals` exceed `k`, move the `left` pointer to the right:
     - If the element at `left` does not match `unique_value`, decrement `removals`.
     - If it matches, decrement `count_same`.
  
5. **Updating the Maximum Score:**
   - After adjusting the window, update `max_score` with the maximum value between the current `max_score` and `count_same`.
  
6. **Final Result:**
   - After iterating through all unique values and maintaining their respective windows, the function returns `max_score`, which represents the maximum k-consistency score.

### Sample Test Case Verification

**Input:**
8 7 5 7 7 1 1 7 7 3
**Output:**
5

**Explanation:**
- By removing the elements `5`, `1`, and `1`, the array becomes `[7, 7, 7, 7, 7]`, which has a maximum of 5 contiguous days with the same return.

### Notes

- This implementation ensures that for each unique value, the maximum number of identical contiguous elements is accurately tracked after removing up to `k` differing elements.
- The `max_score` is updated based on the number of matching elements (`count_same`) within valid windows, ensuring adherence to the problem's requirements.

---

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/downloads/) is recommended to run the provided solutions.

### How to Run the Solutions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ecabanerof/CodingTest.git
   cd CodingTest
   python Test1.py
   python Test2.py

