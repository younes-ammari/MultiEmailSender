# MultEmailSender
**MultEmailSender** is a program that allows user to send email to mult users with one click.

the used programming language was **'PYTHON'** .

i used yagmail to send emails and tkinter in the user interface*

 
 
![screen image](https://user-images.githubusercontent.com/72352932/111909803-fb250b80-8a5e-11eb-8544-8c064155718d.png)



## You need:
1- **Install yagmail** tool in your computer *if you're using the code directly*

if you wanna see how *yagmail* work go this link : **https://github.com/kootenpv/yagmail**



2- **Allow** "Less secure app access" in order to give the yagmail **access** to **use** your email for sending

in order to do that go to this link : **https://myaccount.google.com/lesssecureapps?pli=1** and check the **"Less secure app access"**




## Here is how "yagmail" works:

```python
import yagmail
yag = yagmail.SMTP()
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('to@someone.com', 'subject', contents)
```

Or more simple in just one line:
```python
yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', 'This is the body')
```


### Installing 'yagmail'

For Python 2.x and Python 3.x respectively:

```python
pip install yagmail[all]
pip3 install yagmail[all]

```




### Some Explanations


![screen image descripted](https://user-images.githubusercontent.com/72352932/111909998-d0878280-8a5f-11eb-96c1-ee137f496e66.png)


### ... ان شاء الله يفيدكم
