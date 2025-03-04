# 📌 Markdown Cheat Sheet for Jupyter Notebooks

Markdown is a lightweight markup language used in Jupyter notebooks to format text, add headers, lists, images, and more.

---

## 📌 1. Headers
Use `#` for headings. More `#` means a smaller heading.

```markdown
# H1 - Largest Header
## H2 - Second Largest
### H3 - Medium Header
#### H4 - Smaller Header
##### H5 - Tiny Header
###### H6 - Smallest Header
```

# H1 - Largest Header  
## H2 - Second Largest  
### H3 - Medium Header  
#### H4 - Smaller Header  
##### H5 - Tiny Header  
###### H6 - Smallest Header  

---

## 📌 2. Text Formatting
```markdown
*Italic* or _Italic_
**Bold** or __Bold__
***Bold & Italic*** or ___Bold & Italic___
~~Strikethrough~~
```

*Italic*  
**Bold**  
***Bold & Italic***  
~~Strikethrough~~

---

## 📌 3. Lists

### Unordered List
```markdown
- Item 1
- Item 2
  - Sub-item 2a
  - Sub-item 2b
- Item 3
```

- Item 1  
- Item 2  
  - Sub-item 2a  
  - Sub-item 2b  
- Item 3  

### Ordered List
```markdown
1. First item
2. Second item
   1. Sub-item 1
   2. Sub-item 2
3. Third item
```

1. First item  
2. Second item  
   1. Sub-item 1  
   2. Sub-item 2  
3. Third item  

---

## 📌 4. Links
```markdown
[OpenAI](https://www.openai.com)
```
[OpenAI](https://www.openai.com)

---

## 📌 5. Images
```markdown
![Alt Text](https://via.placeholder.com/150)
```
![Alt Text](https://via.placeholder.com/150)

---

## 📌 6. Code Blocks
### Inline Code
Use backticks for inline code:  
```markdown
`print("Hello, Markdown!")`
```
Output: `print("Hello, Markdown!")`

### Multi-line Code Block
Use triple backticks (```) or indent with 4 spaces:
```markdown
```python
def greet():
    print("Hello, Markdown!")
greet()
```
```

```python
def greet():
    print("Hello, Markdown!")
greet()
```

---

## 📌 7. Blockquotes
Use `>` for blockquotes:
```markdown
> This is a blockquote.
>> Nested blockquote.
```

> This is a blockquote.  
>> Nested blockquote.

---

## 📌 8. Tables
```markdown
| Name  | Age | City     |
|-------|-----|---------|
| Alice | 25  | New York |
| Bob   | 30  | Chicago  |
| Eve   | 22  | San Francisco |
```

| Name  | Age | City         |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Chicago     |
| Eve   | 22  | San Francisco |

---

## 📌 9. Horizontal Line
```markdown
---
```
Output:
---
---

## 📌 10. Math Equations (LaTeX)
```markdown
$E = mc^2$
```
$E = mc^2$

For multi-line equations:
```markdown
$$
F = G rac{m_1 m_2}{r^2}
$$
```
$$
F = G rac{m_1 m_2}{r^2}
$$

---

## 📌 11. Task Lists
```markdown
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
```
- [x] Task 1  
- [ ] Task 2  
- [ ] Task 3  

---

## 📌 12. Escape Characters
Use `\` before a special character to display it as plain text.
```markdown
\*Not Italic\*
```
\*Not Italic\*

---

🚀 **Now you're ready to use Markdown in Jupyter Notebooks!** 🎯
