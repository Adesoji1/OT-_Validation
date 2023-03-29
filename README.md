# OT-Validation
Catching up
When people code together on Replit, everyone's code needs to be in sync. You have to see the same code as I do even though we're typing on different computers. The challenge is making sure we don't end up with a jumbled mess of text while we type together.

So in order to keep everyone's code in sync, Replit uses a method called Operational Transformations, or OT.

Think about OT like this: when you type, you can either insert text, delete text, or move your cursor to a new position (this is called skip in OT land). These actions are called operations, and they transform your document!

More concretely, you can look at an Operational Transformation as a function that takes in a document, a position within that document (like where your cursor is), and then either modifies the document at that position or skips to a new position.

Some examples:
Input document: ""
Starting cursor position: 0
Operation: {"op": "insert", "chars": "Hello, human!"}
Output document: "Hello, human!"
Ending cursor position: 13
Input document: "What is up?"
Starting cursor position: 7
Operation: {"op": "delete", "count": 3}
Output document: "What is?"
Ending cursor position: 7
Watch out: delete operations are applied forward while keeping the cursor in place. Crazy, we know.
Input document: "Nice!"
Starting cursor position: 0
Operation (1): {"op": "skip", "count": 4}
Operation (2): {"op": "insert", "chars": " day"}
Output document: "Nice day!"
Ending cursor position: 8
As you can see, this last example applies two transformations in a row.
What we want you to do
Back to keeping everyone in a multiplayer repl in sync. In the real world, we don't always work at the same time. Sometimes people leave then rejoin later, or lose their internet connection and come back online. When people rejoin, we need their client to "catch up" to the current state of the repl so everyone has the same code in front of them!

So when we catch up, we need to validate that a sequence of operational transformations will actually produce the most recent version of your code. It would be pretty terrible if I edited your file while you're gone, then you somehow end up with the wrong file contents when you rejoin later 😢

For this challenge, you're going to write the OT validation function. The function will take in a string for the stale file contents, a string containing the latest file contents, and a JSON string containing the operations. Your function should validate that the sequence of operations, when applied to the stale contents, produces the latest contents. If it does not, or if the sequence of operations is invalid, your function should return false . The python OT validation function is found on this repository as `Replit_test.py`
