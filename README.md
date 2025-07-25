# NotSoSecure

Making you feel insecure about your password.<br>
These are my approaches to cracking passwords in many different ways.<br>
Started using python, but was quickly reminded how slow and inefficient the language is when it comes to performance intesive tasks.<br>
As this project grows, it will include more and more ways so crack password.<br>
I'll also be switching from python to rust for the aformentioned performance benefits, but I'll leave the python versions here for testing purposes.<br>

This README will mainly be sectioned by the different methods / approaches to password cracking.<br>

---

## Brute Force

#### How it works

If you are unfamiliar with the concept of brute force and want an in depth explanation i would recommend reading [this](https://en.wikipedia.org/wiki/Brute-force_search) wikipedia article.<br>
The article talks about it more generaly but you will get the jist of what we are trying to do here.<br>
In short, in our context brute forcing just means we try every possible combinations of allowed characters as the password until we find it.<br>
As you can imagine this gets reaaally intense for our cpu really fast.<br>
Meaning especially using modern hashing algorithms this approach is not exactly practical in the real world.<br>
I still decided to write an algorithm to see what my cpu can handle :).

#### Python

Once we have all the combinations of characters we need to hash them.<br>
When a password is saved in a database or wherever it is usually (hopefully) not saved as a plain String but as a Hash.<br>
To get said Hash we use a Hashing-Algorithm notably sha-256.<br>
This hashing is what becomes our biggest hurdle when brute forcing since sha-256 has to be run hundreds of millions or even billions of times to hash every single combination.<br>
Since python doesnt natively allow multithreading, due to the GIL (Global Interpreter Lock), we use multiprocessing instead.<br>



