<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - File Handling

## Table of Contents :

  - [0. Read file](#subparagraph0)
  - [1. Write to a file](#subparagraph1)
  - [2. Append to a file](#subparagraph2)
  - [3. Final Quiz](#subparagraph3)
## Introduction and Context

Working with input and output is a fundamental aspect of programming, as it allows programs to interact with external data sources and persist information beyond execution. In Python, this typically involves reading from and writing to files.

This project introduces students to Python’s input/output mechanisms focusing on file manipulation. Students will explore how to open, read, write, and append to files, while also understanding the importance of properly managing file resources.

These concepts are essential for real-world applications, where programs often need to store results, process external data, or communicate with other systems. A solid understanding of input/output operations will also support future learning in areas such as databases, APIs, and data processing pipelines.

It is worth noting that beginners often underestimate edge cases such as file encoding, missing files, or improper resource handling. These aspects should be approached carefully, as they can lead to subtle bugs or data loss if ignored.


## Resources

**Read or watch**:

- [7.2. Reading and Writing Files](/rltoken/1fWMxb6WgEpLGgEHSlmlXw) 
- [8.7. Predefined Clean-up Actions](/rltoken/GGSxHAvz8uhyNxFPmC4AvQ) 
- [Dive Into Python 3: Chapter 11. Files](/rltoken/6Go6e4fJASUxr_OkiwVShg) (*until "11.4 Binary Files" (included)* - Chapter starting in page 263)
- [Learn to Program 8 : Reading / Writing Files](/rltoken/P9xajlsSkvQJWVyW2ng20Q) 

## Learning Objectives
- How to open a file
- How to write text in a file
- How to read the full content of a file 
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`


## Task
### 0. Read file <a name='subparagraph0'></a>

Write a function that reads a text file (`UTF8`) and prints it to stdout:

* Prototype: `def read_file(filename=""):`
* You must use the `with` statement
* You don't need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module

```ruby
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
read_file = __import__('read_file').read_file

read_file("my_file_0.txt")

spam@camelot:~/$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
spam@camelot:~/$ ./main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
spam@camelot:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/file_handling`
* File: `read_file.py`

---

### 1. Write to a file <a name='subparagraph1'></a>

Write a function that writes a string to a text file (`UTF-8`) and returns the number of characters written:

* Prototype: `def write_file(filename="", text=""):`
* You must use the `with` statement
* You don't need to manage file permission exceptions.
* Your function should create the file if doesn't exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module

```ruby
spam@camelot:~/$ cat 1-main.py
#!/usr/bin/env python3
write_file = __import__('write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

spam@camelot:~/$ ./1-main.py
24
spam@camelot:~/$ cat my_first_file.txt
This School is so cool!
spam@camelot:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/file_handling`
* File: `write_file.py`

---

### 2. Append to a file <a name='subparagraph2'></a>

Write a function that appends a string at the end of a text file (`UTF-8`) and returns the number of characters added:

* Prototype: `def append_write(filename="", text=""):`
* If the file doesn't exist, it should be created
* You must use the `with` statement
* You don't need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module

```ruby
spam@camelot:~/$ cat 2-main.py
#!/usr/bin/env python3
append_write = __import__('append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

spam@camelot:~/$ cat file_append.txt
cat: file_append.txt: No such file or directory
spam@camelot:~/$ ./2-main.py
24
spam@camelot:~/$ cat file_append.txt
This School is so cool!
spam@camelot:~/$ ./2-main.py
24
spam@camelot:~/$ cat file_append.txt
This School is so cool!
This School is so cool!
spam@camelot:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_advanced/file_handling`
* File: `append_write.py`

---

### 3. Final Quiz <a name='subparagraph3'></a>

### Instructions

You have reached the end of this project on file handling in Python. At this stage, you are expected to be comfortable working with files using the core operations: reading, writing, and appending.

This quiz is designed to validate your understanding of these concepts, as well as your ability to reason about how file operations behave in different scenarios. You will encounter questions that test both your knowledge of Python syntax and your understanding of underlying behaviors such as file modes, resource management, and common sources of errors.

Each question has a limited time to be answered, typically between **45 and 60 seconds**. This constraint is intentional: it encourages you to rely on solid understanding rather than trial-and-error reasoning.

This is a **one-shot quiz**, meaning you have a single attempt to complete it. There are no retries, so it is important to read each question carefully before answering.

Some questions may require selecting more than one correct answer. Read each question carefully and ensure that your selections fully reflect your understanding.

Be aware that superficial familiarity with functions like `open()`, `read()`, or `write()` is often not sufficient. Many mistakes in real-world code arise from misunderstandings about how file modes work or how files are managed in memory. This quiz aims to surface those gaps.

Take your time within the allowed limits and approach each question deliberately.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
