<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/rfulkerson/25spring1400/blob/main/ai_for_cs1.md">Using AI Responsibly for CS1</a> &copy; 2025 by <span property="cc:attributionName">Robert Fulkerson</span> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

**Last updated April 15, 2025. This is a work in progress.**

# Using AI Responsibly for CS1

What we learn in a CS1 course -- all of the basic syntax, concepts, and computational thinking -- is foundational material for understanding how to think about solving problems with programming, write your own code, debug your own code and code that others have written. In the ever-evolving world of Artificial Intelligence (AI) and Large Language Models (LLMs) -- hereafter simply refered to as AI -- work with them to create, analyze, and debug generated code

As students taking an introductory computer science course, you should have a fundamental understanding of the code that we're writing ourselves and that AI is writing for us, sometimes in the scope of ten lines of code or even hundreds or thousands of lines of code.

You should treat the AI as a suggestion engine. Your job as a computer scientist and Computer Science 1 (CS1) student is to verify, adapt, and learn from those suggestions.

---

## Tasks that AI can be useful for in CS1

Since the release of ChatGPT in 2022 and its meteoric rise to widespread adoption and acceptance in many industries and sectors, especially education, many students have seen AI as a simple solution engine, pasting assignments into any number of AI engines and having those services generate passable solutions that they then submit as "homework".

Unless the teacher explicitly states that a student should use AI, there is an obvious disconnect with what is intended by the instructor and how the student is engaging with the material. Simple copy/paste behavior of assignments into AI engines bypasses the carefully structured assignment developed by the teacher, likely intended to either scaffold the student to the next level of or assess their current understanding of the material.

Even if AI is not explicitly allowed or approved for use on an assignment, there are a number of ways that AI can be used productively for learing materials in a CS1 course.

Below are some of many numerous possibilities. 

Click on a task area for more information or continue scrolling to see detailed discussions and sample prompts for each area.

Task | Usefulness | Basic Tips
:-- | :-- | :--
[Research a topic further](#research)|  Practice prompting, interacting with results, and evaluating sources. |  Cross-check at least one claim outside of the AI/LLM to deepend your understanding.
Generate code to debug |  Debugging is a core CS1 skill. |  Ask the LLM to not label or identify bugs.
[Interactive quiz / review](#review) |  Great for getting different versions of questions about topics you're learning. |  Frame the review in terms of CS1 and cross-check questions.
Brainstorm personal projects |  Personal interest drives active and engaged learning and leads to rewarding results. |   Frame idea generation in terms of CS1 skills and have the AI evaluate your project code.
<a href="#assigns">Assignment guidance without code</a> |  AI can outline tasks and make suggestions about how to approach a problem. |   Analyze your own thinking against what the AI suggests.
Stubbed-out larger project |  Mimics industry practice of inheriting partial codebases. |   Frame in terms of CS1 skills, have AI create project for you to complete.

---

### <a name="research">Using AI to Research a Topic Further</a>

Here are some example prompts you could use as guidance for your own questions:

Goal |  Example prompt 
:-- | :--
Concept clarification |  Can you explain the concept of type in Python? Assume I only know CS1 materials.
Debugging help | I'm getting a TypeError when I run this code. Can you help me understand what's wrong?<br><br>`grades = [88, 92, 79]` <br>`average = 0`<br>`for g in grades:`<br>`    average += g`<br>`    print("Average: " + average / len(grades))`
Design guidance | I need to store student scores. Which built-in Python type would be most appropriate and why?
Step-by-step hint | I'm stuck on converting a string like `'1,149'` to an integer. Don't give me the final code, but can you nudge me in the right direction?

Thoughts:

* **Emphasize minimal, runnable examples.** Paste only what's necessary so that the feedback is focused.
* **Ask for explanations first, code only if necessary.** "Explain why my loop is off-by-one before suggesting a fix."
* **Compare AI advice to official docs.** Cross-check functions/code/results with official documentation/requirements, building healthy skepticism.
* **Reflect aloud.** After the AI's answer, paraphrase out loud what your takeaway is. ([Rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging))

<hr>

### <a name="review">Interactive Quiz / Review</a>

Using an AI for quiz or concept review can be done simply or in a more detailed manner. The prompt you use can guide your experience with the review.

Here's an example of a simple prompt that generates some questions for review:

> Hi. I'm taking a CS1 course and we have a quiz coming up soon about functions and strings. Can you prompt me with about 15 questions appropriate for a CS1 course and check my correctness?

And here's a more detailed prompt that specifies exact parameters of the content and the types of questions. The topics section would be modified for the specific material being studied.

> I'm studying for a CS1 quiz that will cover functions, strings, lists, and dictionaries in Python. Could you create a 15-question practice quiz that mixes multiple-choice, short-answer, code-writing, and conceptual/explanation questions focused on key concepts from these topics?
>
> Topics should include but not be limited to:
> * Defining and calling functions
> * Parameters, arguments, and return values
> * Default parameters and keyword arguments
> * Returning multiple values from a function
> * String manipulation (e.g., indexing, slicing, concatenation, etc.)
> * String methods (e.g., upper(), lower(), strip(), etc.)
> * Lists: indexing, appending, slicing, and basic iteration
> * Dictionaries: creating key-value pairs, accessing/modifying values, basic iteration
> * Conceptual understanding of how functions, strings, lists, and dictionaries behave in Python (e.g., parameter passing, immutability vs. mutability, reference vs. copy, what it means to return a value, etc.)
> 
> Please exclude questions involving error handling or try/except blocks, as those are not covered at this level.
>
> After each question, please allow me to answer and provide feedback on my response before moving on to the next question.
> 
> If presenting code, please format it with multiple lines for clarity.
>
> At the end, please provide a summary of my performance with suggestions on areas to review and areas of strength.

---

### <a name="assigns">Assignment Guidance</a>

Probably the most widely used aspect of AI today for a CS1 student is copying and pasting an assignment's specifications into an AI to have it simply write code to solve the problem for them.

There's zero learning in that situation, and you're not preparing yourself for more advanced coursework int he future that will require you to think deeply and critically about how to implement a solution to a problem or how to analyze content that is generated by an AI assistant.

*A different way to approach this situation is to use the AI as a suggestion engine and competent CS tutor.*

Here is a sample prompt with a well-defined [system message](https://promptmetheus.com/resources/llm-knowledge-base/system-message) and [user section](https://www.nebuly.com/blog/llm-system-prompt-vs-user-prompt) that you could use to set up a useful and interacative session. You would replace the actual assignment specification at the end of this example with a relevant assignment or problem to work through.

>You are a friendly CS1‑level Python tutor. Your job is to guide me through the problem‑solving process *without providing any code, pseudocode, or step‑by‑step algorithmic solution*.
>
> * Use plain language appropriate for a first‑semester programming student.
> * Limit jargon; if a technical term is necessary, give a short definition in parentheses.
> * Favor concrete examples that involve basic Python concepts (variables, loops, lists, functions) and avoid advanced topics (classes, recursion, decorators, exceptions) unless I explicitly ask.
> * Encourage me to think aloud and verify my own understanding.
> * End each reply with one “check‑your‑understanding” question I can answer before we continue.
>
> What I need from you:
> 
> 1. Plain‑English summary – Restate the task so I can confirm my understanding.
> 2.	Key elements – List inputs, outputs, and constraints.
> 3.	Conceptual roadmap – Suggest high‑level strategies or data structures I might explore (no code).
> 4.	Guiding questions – Ask me what I should consider (edge cases, tests, pitfalls).
> 5.	Forbidden content – No code, pseudocode, or exact algorithmic steps.
> 6.	Check‑back option – Tell me how I can follow up once I’ve tried something.
> 7.	(Reminder) – Please keep explanations at a CS1 beginner level.
>
> Assignment Description:
> 
> An acronym is a word formed from the initial letters of words in a given phrase. Write a program whose input is a phrase and whose output is an appropriate acronym of the input. Append a period (`.`) after each letter in the acronym. Acronyms should only be built from words that start with capital letters. You can assume the input has at least one word that starts with upper case letter.
> 
> Ex: If the input is:
>
> `As Soon As Possible`
>
> the output is:
>
> `A.S.A.P.`
>
> Ex: If the input is:
>
> `Completely Automated Public Turing tEST to tell COMPUTERS and Humans Apart`
>
> the output is:
> 
> `C.A.P.T.C.H.A.`
>
> Although the letters `OMPUTERS` in `COMPUTERS` are upper case, those letters are not processed for the acronym for being a part of the word `COMPUTERS`. Similarly, even though `EST` in the word `tEST` are capitalized, they are not processed because the program should only pay attention to the first letter of the word.

Here's are some reasons that a prompt like this works so well:

Item/Directive | Purpose/Result
:-- | :--
Initial system message |Gives the model a hard boundary: "No code."
"CS1-level Python tutor" | Signals the target audience and expected depth.
Plain-English summary | Lets you verify that you and the AI interpret the prompt the same way.
Key elements | Helps you isolate inputs/outputs before thinking about design.
Conceptual roadmap | Encourages AI to generate content prompting you to think in [abstractions](https://www.learning.com/blog/abstraction-in-computational-thinking/) (loops, lists, dictionaries) without being given answers.
Guiding questions | Promotes [metacognition](https://tll.mit.edu/teaching-resources/how-people-learn/metacognition/#:~:text=Metacognition%20is%20the%20process%20by%20which%20learners%20use%20knowledge%20of%20the%20task%20at%20hand%2C%20knowledge%20of%20learning%20strategies%2C%20and%20knowledge%20of%20themselves%20to%20plan%20their%20learning%2C%20monitor%20their%20progress%20towards%20a%20learning%20goal%2C%20and%20then%20evaluate%20the%20outcome.%C2%A0) and a checklist mindset.
Forbidden content | Reinforces the no-code rule and reduces policy slip-ups.
Jargon limiter + parenthetical defs | Prevents overwhelm and builds vocabulary gradually.
Scope boundaries (avoid classes/recursion/exceptions) | Keeps the discussion aligned with the course.
Check-your-understanding question | Promotes active learning and gives you a natural pause to reflect.
Beginner-level reminder in User section | Redundancy that further reduces drift into advanced territory.

Here are some tips you can keep in mind while working with this type of prompt:

1.	**Iterate safely** – If the model starts drifting into code, you should be able to redirect it with: 
"Please remove any code from future responses and stick to conceptual guidance."
1. **Be explicit** – If you later paste partial code into the discussion for debugging, prepend it with:
"Please only identify logical errors or misconceptions; do not rewrite the code for me."
3.	**Cross‑verify** – You should critically compare the AI’s initial summary with the original specification. Any mismatch is a red flag that something is off and needs clarification—whether that’s the AI’s reading, your own understanding, or the specification itself.
4.	**Focus on learning, not copying** – Interactions with the AI should be considered as class notes or tutor dialogue that you should contemplate in formulating your own solution, not turned in as your own work.

Here are some extras you can add in to modify the AI's behavior even further (add these to the "What I need from you" section):

1.	**Word‑count ceiling**: "Keep each answer under 250 words so that I’m not flooded with information."
2.	**[Bloom’s Taxonomy](https://www.youtube.com/watch?v=ve-Evb5bGoc) scaffolding**: "Frame your guiding questions to progress from recall → apply → analyze."
3.	**Tone cue**: "Use a warm, encouraging tone and celebrate small insights."

---
