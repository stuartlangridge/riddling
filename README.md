Riddling
========

Riddling: A puzzle game involving intelligence, psychology, lateral thinking, research, and guesswork. For Google fiends, librarians, mathematicians, linguists, and pub quiz winners. 

Cross-platform with PhoneGap.

Designed to be built with PhoneGap Build. Create new icons with the make_icons.py script, which requires imagemagick to be around.

To set riddle answers, cd resources && node hash-riddles.js. This requires riddles-unhashed.js, which is the actual list of answers and looks like:

    exports.riddles = [
        {},
        { clue: "", answer: "1" },
        { clue: "one", answer: "two",
            explanation: "Good one! You worked out that if ‘one’ is the answer for Level 1, that ‘two’ must be it for Level 2. Now try to get to the next level." },
        ...
    ];
    exports.universal = "text which acts as a cheat's correct answer";

