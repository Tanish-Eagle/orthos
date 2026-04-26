## Orthos:

Orthos is a spelling and grammar checker, built on top of LanguageTool. It runs in the command line, giving you options such as enter a number to pick one of the generated fixes; Skipping or ignoring a suggestion for the current session; And adding a particular word to a custom dictionary of your own, for specialized writing with its own terms and words.

## Getting LanguageTool:

Before you run Orthos, you will need LanguageTool. You will need to run it as a local server. LanguageTool requires Java on your machine, so I suggest you install any long-term supported version of Open JDK.

You can download LanguageTool from [this page.](https://languagetool.org/download/)

Unzip it, and then run this command:

```
java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
```

Once it is up and running, leave it. After this step is done, you are ready to run Orthos.

## To run Orthos:

For now, you can clone the repository, set up a virtual environment, install the requirements from requirements.txt by using the following command:

```
pip install -r requirements.txt
```

Then, you can turn this into a package:

```
pip install -e .
```

After that, you can type the command to activate Orthos:

```
Orthos filename.txt
```

And that is it. Once the file loads, you will see the suggestions on your screen, and then you can process them one by one. After you go through all the text in your file, your file will be updated with the suggestions you have chosen.

Warning! It means your file will be modified! Keep a copy of the original file, just in case.

It is a rather roundabout way to run this, but for now, I am not distributing it as a package.

## My motivation to build Orthos:

I needed a non-AI based solution which runs in the command line, which does not interfere with my writing tone. With Orthos, I get both. I get the grammar checking I require, but my tone remains intact. It is very light, so I can run on my laptop. It is a command line application, so it is very accessible to me.

Quite honestly, it is a personal project designed for personal usage. I'm just putting it out here because I think it is good enough to show off in the public.


## The inspiration of the name:

Orthos is inspired by Orthography, which is a set of conventions about how to write a language, including its spelling and grammar, word boundaries, and even the punctuation.

Another reason why I picked this name is because of Orthos, the fire turtle from Cradle Series by the author Will Wight. I am a huge fan of that series.