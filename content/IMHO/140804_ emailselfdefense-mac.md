Title: 电邮的自我防护
Date: 2014-08-03 
Tags: fsf,Pythoneer,Zh 
Slug: 140718-fsf-emailselfdefense-mac

[TOC]

![](https://static.fsf.org/nosvn/enc-dev0/img/en/infographic-button.png)

[Email Self-Defense - a guide to fighting surveillance with GnuPG encryption](https://emailselfdefense.fsf.org/en/mac.html)


Bulk surveillance violates our fundamental rights and makes free speech risky. This guide will teach you a basic surveillance self-defense skill: email encryption. Once you've finished, you'll be able to send and receive emails that are coded to make sure a surveillance agent or thief intercepting your email can't read it. All you need is a computer with an Internet connection, an email account, and about half an hour.




Even if you have nothing to hide, using encryption helps protect the privacy of people you communicate with, and makes life difficult for bulk surveillance systems. If you do have something important to hide, you're in good company; these are the same tools that Edward Snowden used to share his famous secrets about the NSA.

In addition to using encryption, standing up to surveillance requires fighting politically for 
[a reduction in the amount of data collected on us](http://gnu.org/philosophy/surveillance-vs-democracy.html)
, but the essential first step is to protect yourself and make surveillance of your communication as difficult as possible. Let's get started!

## #1 GET THE PIECES
This guide relies on software which is freely licensed; it's completely transparent and anyone can copy it or make their own version. This makes it safer from surveillance than proprietary software (like Mac OS). To defend your freedom as well as protect yourself from surveillance, we recommend you switch to a free software operating system like GNU/Linux. Learn more about free software at fsf.org.

To get started, you'll need a desktop email program installed on your computer. This guide works with free software versions of the Thunderbird email program, and with Thunderbird itself. Email programs are another way to access the same email accounts you can access in a browser (like Gmail), but provide extra features.

If you already have one of these, you can skip to Step 1.b.

### Step 1.A: Install Wizard
STEP 1.A
SETUP YOUR EMAIL PROGRAM WITH YOUR EMAIL ACCOUNT (IF IT ISN'T ALREADY)
Open your email program and follow the wizard that sets it up with your email account.
TROUBLESHOOTING
What's a wizard?
A wizard is a series of windows that pop up to make it easy to get something done on a computer, like installing a program. You click through it, selecting options as you go.
My email program can't find my account or isn't downloading my mail
Before searching the Web, we recommend you start by asking other people who use your email system, to figure out the correct settings.
Don't see a solution to your problem? Please let us know on the feedback page.

### STEP 1.B
GET GNUPG BY DOWNLOADING GPGTOOLS
GPGTools is a software package that includes GnuPG. Download and install it, choosing default options whenever asked. After it's installed, you can close any windows that it creates.
Step 1.C: Tools -> Add-onsStep 1.C: Search Add-onsStep 1.C: Install Add-ons

### STEP 1.C
INSTALL THE ENIGMAIL PLUGIN FOR YOUR EMAIL PROGRAM
In your email program's menu, select Add-ons (it may be in the Tools section). Make sure Extensions is selected on the left. Do you see Enigmail? if so, skip this step.
If not, search "Enigmail" with the search bar in the upper right. You can take it from here. Restart your email program when you're done.
TROUBLESHOOTING

## #2 MAKE YOUR KEYS
To use the GnuPG system, you'll need a public key and a private key (known together as a keypair). Each is a long string of randomly generated numbers and letters that are unique to you. Your public and private keys are linked together by a special mathematical function.

Your public key isn't like a physical key, because it's stored in the open in an online directory called a keyserver. People download it and use it, along with GnuPG, to encrypt emails they send to you. You can think of the keyserver as phonebook, where people who want to send you an encrypted email look up your public key.

Your private key is more like a physical key, because you keep it to yourself (on your computer). You use GnuPG and your private key to decode encrypted emails other people send to you.

### Step 2.A: Make a Keypair
STEP 2.A
MAKE A KEYPAIR
In your email program's menu, select OpenPGP → Setup Wizard. You don't need to read the text in the window that pops up unless you'd like to, but it's good to read the text on the later screens of the wizard.
On the second screen, titled "Signing," select "No, I want to create per-recipient rules for emails that need to be signed."
Use the default options until you reach the screen titled "Create Key".
On the screen titled "Create Key," pick a strong password! Your password should be at least 12 characters and include at least one lower case and upper case letter and at least one number or punctuation symbol. Don't forget the password, or all this work will be wasted!
The program will take a little while to finish the next step, the "Key Creation" screen. While you wait, do something else with your computer, like watching a movie or browsing the Web. The more you use the computer at this point, the faster the key creation will go.
When the OpenPGP Confirm screen pops up, select Generate Certificate and choose to save it in a safe place on your computer (we recommend making a folder called "Revocation Certificate" in your home folder and keeping it there). You'll learn more about the revocation certificate in Section 5. The setup wizard will ask you to move it onto an external device, but that isn't necessary at this moment.
TROUBLESHOOTING

### STEP 2.B
UPLOAD YOUR PUBLIC KEY TO A KEYSERVER
In your email program's menu, select OpenPGP → Key Management.
Right click on your key and select Upload Public Keys to Keyserver. Use the default keyserver in the popup.
Now someone who wants to send you an encrypted message can download your public key from the Internet. There are multiple keyservers that you can select from the menu when you upload, but they are all copies of each other, so it doesn't matter which one you use. However, it sometimes takes a few hours for them to match each other when a new key is uploaded.
TROUBLESHOOTING

### GNUPG, OPENPGP, WHAT?
You're using a program called GnuPG, but the menu in your email program is called OpenPGP. Confusing, right? In general, the terms GnuPG, GPG, GNU Privacy Guard, OpenPGP and PGP are used interchangeably, though they all have slightly different meanings.

## #3 TRY IT OUT!
Now you'll try a test correspondence with a computer program named Edward, which knows how to use encryption. Except where noted, these are the same steps you'd follow when corresponding with a real, live person.

Try it out.
### STEP 3.A
SEND EDWARD YOUR PUBLIC KEY
This is a special step that you won't have to do when corresponding with real people. In your email program's menu, go to OpenPGP → Key Management. You should see your key in the list that pops up. Right click on your key and select Send Public Keys by Email. This will create a new draft message, as if you had just hit the Write button.
Address the message to edward-en@fsf.org. Put at least one word (whatever you want) in the subject and body of the email, then hit send.
It may take two or three minutes for Edward to respond. In the meantime, you might want to skip ahead and check out the Use it Well section of this guide. Once he's responded, head to the next step. From here on, you'll be doing just the same thing as when corresponding with a real person.
### STEP 3.B
SEND A TEST ENCRYPTED EMAIL
Write a new email in your email program, addressed to edward-en@fsf.org. Make the subject "Encryption test" or something similar and write something in the body. Don't send it yet.
Click the icon of the key in the bottom right of the composition window (it should turn yellow). This tells Enigmail to encrypt the email.
Next to the key, you'll notice an icon of a pencil. Clicking this tells Enigmail to add a special, unique signature to your message, generated using your private key. This is a separate feature from encryption, and you don't have to use it for this guide.
Click Send. Enigmail will pop up a window that says "Recipients not valid, not trusted or not found."
To encrypt an email to Edward, you need his public key, so now you'll have Enigmail download it from a keyserver. Click Download Missing Keys and use the default in the pop-up that asks you to choose a keyserver. Once it finds keys, check the first one (Key ID starting with C), then select ok. Select ok in the next pop-up.
Now you are back at the "Recipients not valid, not trusted or not found" screen. Select Edward's key from the list and click Ok. If the message doesn't send automatically, you can hit send now.
TROUBLESHOOTING

#### IMPORTANT:
SECURITY TIPS
Even if you encrypted your email, the subject line is not encrypted, so don't put private information there. The sending and receiving addresses aren't encrypted either, so they could be read by a surveillance system. When you send attachments, Enigmail will give you an option of whether you want to encrypt them.
It's also good practice to click the key icon in your email composition window before you start to write. Otherwise, your email client could save an unencrypted draft on the mail server, potentially exposing it to snooping.

### STEP 3.C
RECEIVE A RESPONSE
When Edward receives your email, he will use his private key to decrypt it, then fetch your public key from a keyserver and use it to encrypt a response to you.
Since you encrypted this email with Edward's public key, Edward's private key is required to decrypt it. Edward is the only one with his private key, so no one except him — not even you — can decrypt it.
It may take two or three minutes for Edward to respond. In the meantime, you might want to skip ahead and check out the Use it Well section of this guide.
When you receive Edward's email and open it, Enigmail will automatically detect that it is encrypted with your public key, and then it will use your private key to decrypt it.
Notice the bar that Enigmail shows you above the message, with information about the status of Edward's key.

## #4 LEARN THE WEB OF TRUST
Email encryption is a powerful technology, but it has a weakness; it requires a way to verify that a person's public key is actually theirs. Otherwise, there would be no way to stop an attacker from making an email address with your friend's name, creating keys to go with it and impersonating your friend. That's why the free software programmers that developed email encryption created keysigning and the Web of Trust.

When you sign someone's key, you are publicly saying that you trust that it does belong to them and not an impostor. People who use your public key can see the number of signatures it has. Once you've used GnuPG for a long time, you may have hundreds of signatures. The Web of Trust is the constellation of all GnuPG users, connected to each other by chains of trust expressed through signatures, forming a giant network. The more signatures a key has, and the more signatures its signers' keys have, the more trustworthy that key is.

People's public keys are usually identified by their key fingerprint, which is a string of digits like F357AA1A5B1FA42CFD9FE52A9FF2194CC09A61E8 (for Edward's key). You can see the fingerprint for your public key, and other public keys saved on your computer, by going to OpenPGP → Key Management in your email program's menu, then right clicking on the key and choosing Key Properties. It's good practice to share your fingerprint wherever you share your email address, so that people can double-check that they have the correct public key when they download yours from a keyserver.

You may also see public keys referred to by their key ID, which is simply the last 8 digits of the fingerprint, like C09A61E8 for Edward. The key ID is visible directly from the Key Management Window. This key ID is like a person's first name (it is a useful shorthand but may not be unique to a given key), whereas the fingerprint actually identifies the key uniquely without the possibility of confusion. If you only have the key ID, you can still look up the key (as well as its fingerprint), like you did in Step 3, but if multiple options appear, you'll need the fingerprint of the person to whom are trying to communicate to verify which one to use.

## Section 4: Web of Trust
### STEP 4.A
SIGN A KEY
In your email program's menu, go to OpenPGP → Key Management.
Right click on Edward's public key and select Sign Key from the context menu.
In the window that pops up, select "I will not answer" and click ok.
In your email program's menu, go to OpenPGP → Key Management → Keyserver → Upload Public Keys and hit ok.
You've just effectively said "I trust that Edward's public key actually belongs to Edward." This doesn't mean much because Edward isn't a real person, but it's good practice.

#### IMPORTANT:
CHECK PEOPLE'S IDENTIFICATION BEFORE SIGNING THEIR KEYS
Before signing a real person's key, always make sure it actually belongs to them, and that they are who they say they are. Ask them to show you their ID (unless you trust them very highly) and their public key fingerprint -- not just the shorter public key ID, which could refer to another key as well. In Enigmail, answer honestly in the window that pops up and asks "How carefully have you verified that the key you are about to sign actually belongs to the person(s) named above?".

## #5 USE IT WELL
Everyone uses GnuPG a little differently, but it's important to follow some basic practices to keep your email secure. Not following them, you risk the privacy of the people you communicate with, as well as your own, and damage the Web of Trust.

Section 5: Use it Well

### WHEN SHOULD I ENCRYPT?
The more you can encrypt your messages, the better. If you only encrypt emails occasionally, each encrypted message could raise a red flag for surveillance systems. If all or most of your email is encrypted, people doing surveillance won't know where to start.
That's not to say that only encrypting some of your email isn't helpful -- it's a great start and it makes bulk surveillance more difficult.
Section 5: Use it Well

#### IMPORTANT:
BE WARY OF INVALID KEYS
GnuPG makes email safer, but it's still important to watch out for invalid keys, which might have fallen into the wrong hands. Email encrypted with invalid keys might be readable by surveillance programs.
In your email program, go back to the second email that Edward sent you. Because Edward encrypted it with your public key, it will have a message from OpenPGP at the top, which most likely says "OpenPGP: Part of this message encrypted."
When using GnuPG, make a habit of glancing at that bar. The program will warn you there if you get an email encrypted with a key that can't be trusted.

### COPY YOUR REVOCATION CERTIFICATE TO SOMEWHERE SAFE
Remember when you created your keys and saved the revocation certificate that GnuPG made? It's time to copy that certificate onto the safest digital storage that you have -- the ideal thing is a flash drive, disk, or hard drive stored in a safe place in your home.
If your private key ever gets lost or stolen, you'll need this certificate file to let people know that you are no longer using that keypair.

#### IMPORTANT:
ACT SWIFTLY IF SOMEONE GETS YOUR PRIVATE KEY
If you lose your private key or someone else gets ahold of it (say, by stealing or cracking your computer), it's important to revoke it immediately before someone else uses it to read your encrypted email. This guide doesn't cover how to revoke a key, but you can follow the instructions on the GnuPG site. After you're done revoking, send an email to everyone with whom you usually use your key to make sure they know.

## GREAT JOB! CHECK OUT THE NEXT STEPS.
Free Software Foundation

Copyright © 2014 Free Software Foundation, Inc. Privacy Policy. Join.
Version 2.1. Source code of Edward reply bot by Josh Drake <zamnedix@gnu.org> available under the GNU General Public License.
The images on this page are under a Creative Commons Attribution 4.0 license (or later version), and the rest of it is under a Creative Commons Attribution-ShareAlike 4.0 license (or later version). — Why these licenses?
Download the source package for this guide. Fonts used in the guide & infographic: Dosis by Pablo Impallari, Signika by Anna Giedryś, Archivo Narrow by Omnibus-Type, PXL-2000 by Florian Cramer.
JavaScript license information

 

## Changlog

- 1408?? 
- 140803 偶遇抄转
 