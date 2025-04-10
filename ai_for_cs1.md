# Using AI and LLMs responsibly for a CS1 course like CIST 1400

Even with AI/LLMs available to us, as CS1 students, we should want to understand the code we're writing.

What we're learning here in CS1 is foundational material for understanding how to write your own code, debug code others have written, and work with AI/LLMs to create, analyze, and debug code.

Treat the AI/LLM as a suggestion engine. Your job is to verify, adapt, and learn from those suggestions.

## Generalized Tasks for AI in CS1

Task | Reason | Tips
:-- | :-- | :--
[Research a topic further](#research)|  Practice prompting, interacting with results, and evaluating sources. |  Cross-check at least one claim outside of the AI/LLM.
Generate code to debug |  Debugging is a core CS1 skill. |  Ask the LLM to not label or identify bugs.
[Interactive quiz / review](#review) |  Great for getting different versions of questions about topics you're learning. |  Frame the review in terms of CS1 and cross-check questions.
Brainstorm personal projects |  Personal interest drives active and engaged learning and leads to rewarding results. |   Frame in terms of CS1 skills and have LLM evaluate your project code.
Analyze assignment spec (without code) |  AI can outline tasks and make suggestions about how to approach a problem. |   Analyze your own thinking against what the AI suggests.
Stubbed-out larger project |  Mimics industry practice of inheriting partial codebases. |   Frame in terms of CS1 skills, have AI create project for you to complete.

<hr>

### <a name="research">Using AI to Research a Topic Further</a>

Here are some example prompts you could use as guidance for your own questions:

Goal |  Example prompt 
:-- | :--
Concept clarification |  Can you explain the concept of type in Python? Assume I only know CS1 materials.
Debugging help | I'm getting a TypeError when I run this snippet. Can you help me understand what's wrong? (Then paste only the minimal failing snippet, adding more code for context if necessary).<br><br>Example code to paste with question:<br>`grades = [88, 92, 79]` <br>`average = 0`<br>`for g in grades:`<br>`    average += g`<br>`    print("Average: " + average / len(grades))`
Design guidance | I need to store student scores. Which built-in Python type would be most appropriate and why?
Step-by-step hint | I'm stuck on converting a string like '1,149' to an integer. Don't give me the final code, but can you nudge me in the right direction?

Thoughts:

* **Emphasize minimal, runnable examples.** Paste only what's necessary so that feedback is focused.
* **Ask for explanations first, code second.** "Explain why my loop is off-by-one before suggesting a fix."
* **Compare AI advice to official docs.** Cross-check functions/code/results with official documentation/requirements, building healthy skepticism.
* **Reflect aloud.** After the AI's answer, paraphrase out loud what your takeaway is. (Rubber duck debugging)

<hr>

### <a name="review">Interactive Quiz / Review</a>

Using an AI/LLM for quiz or concept review can be done simply or in a more detailed manner.

Here's an example of a simple prompt that generates some questions for review:

> Hi. I'm taking a CS1 course and we have a quiz coming up soon about functions and strings. Can you prompt me with about 15 questions appropriate for a CS1 course and check my correctness?

And here's a more detailed prompt that specifies exact parameters of the content and the types of questions:

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
> After each question, please allow me to answer and provide feedback on my response.
> 
> If presenting code, please format it with multiple lines for clarity.
>
> At the end, please provide a summary of my performance with suggestions on areas to review.
> 
> Thanks!

<hr>

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/rfulkerson/25spring1400/blob/main/ai_for_cs1.md">Using AI Responsibly for CS1</a> by <span property="cc:attributionName">Robert Fulkerson</span> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
