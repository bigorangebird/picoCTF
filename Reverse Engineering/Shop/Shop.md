# Shop
- Category : Reverse Engineering
- Points 50

### Description

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/db20ea321ce780e69e29fd4b60e60fe0/source). The shop is open for business at nc mercury.picoctf.net 3952


### Downloads
[source](./source)


### Hints

1. Always check edge cases when programming


## Overview

Another challenge with no real direction provided other than the suggestion that we need to 'Buy-buy-buy' and to check edge-cases.


## Steps

1. Okay... let's start by looking at the web service at *nc mercury.picoctf.net 3952*

   ```
   > nc mercury.picoctf.net 3952
   Welcome to the market!
   =====================
   You have 40 coins
   	Item		Price	Count
   (0) Quiet Quiches	10	12
   (1) Average Apple	15	8
   (2) Fruitful Flag	100	1
   (3) Sell an Item
   (4) Exit
   Choose an option:    
   ```

   And by downloading the provided file using wget
   ```
   wget https://mercury.picoctf.net/static/db20ea321ce780e69e29fd4b60e60fe0/source
   ```


2. The downloaded file isn't source code,

   ```
   file source
source: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, Go BuildID=Wq2z6hkBrrAovu6w8dMb/chyUPt3_NgRB5zVfMpf8/99tYvdYHy3xNdHp4wuxA/ClEGFX9e3WU6qjzPxg9K, with debug_info, not stripped
   ```

   Rather, it is an executable .... but it is interesting to note that *debug_info* is mentioned ... so it might be that we can glean some useful information from a debugger (if we only knew how to use one).


3. Ok; so what is this challenge trying to get us to do?

   ```
   >nc mercury.picoctf.net 3952
   Welcome to the market!
   =====================
   You have 40 coins
   	Item		Price	Count
   (0) Quiet Quiches	10	12
   (1) Average Apple	15	8
   (2) Fruitful Flag	100	1
   (3) Sell an Item
   (4) Exit
   Choose an option:
   > 2
   How many do you want to buy?
   > 1
   Not enough money.
   ```

   Looking at the initial output from the service - it seems we start with 40 coins, and there is a purchase option with a price of 100. So perhaps we are supposed to cause our wallet of 40 coins to increase somehow.

   The hint suggests that edge-inputs are the thing to try.

   So let's start by seeing how the web-service reacts if we use some daft inputs.


4. Entering *-1* or *5* at the menu; the service simply exits

   Ok, so lets select a valid product to buy, and try edge cases there

   ```
   You have 40 coins
      Item      		Price	Count
    (0) Quiet Quiches	10	12
    (1) Average Apple	15	8
    (2) Fruitful Flag	100	1
    (3) Sell an Item
    (4) Exit
    Choose an option:
    > 0
    How many do you want to buy?
    > -1
    You have 50 coins
     Item		Price	Count
    (0) Quiet Quiches	10	13
    (1) Average Apple	15	8
    (2) Fruitful Flag	100	1
    (3) Sell an Item
    (4) Exit
    Choose an option:

   ```

   Ah ha ... we purchased -1 of the Quiet Quiches ... and our wallet increased by the value of product.
   The developer has obviously calculated

    *New Wallet Value = Old Wallet Value - (Product Cost * Qty)*

  Which would be totally reasonable, but only if Qty is greater than 1 ... otherwise deducting the sale cost will be deducting a negative value ... resulting in an 'payment' into our wallet.


5. So, let's exploit this - and cause our wallet to swell sufficiently to buy a Fruitful flag

  ```
  You have 50 coins
  	Item		Price	Count
  (0) Quiet Quiches	10	13
  (1) Average Apple	15	8
  (2) Fruitful Flag	100	1
  (3) Sell an Item
  (4) Exit
  Choose an option:
  > 0
  How many do you want to buy?
  > -10
  You have 150 coins
  	Item		Price	Count
  (0) Quiet Quiches	10	23
  (1) Average Apple	15	8
  (2) Fruitful Flag	100	1
  (3) Sell an Item
  (4) Exit
  Choose an option:  
  ```

  Woo hoo, we now have enough to buy a Fruitful Flag.

  ```
  You have 150 coins
    	Item		Price	Count
    (0) Quiet Quiches	10	23
    (1) Average Apple	15	8
    (2) Fruitful Flag	100	1
    (3) Sell an Item
    (4) Exit
    Choose an option:
    > 2
    How many do you want to buy?
    > 1
    Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 57 99 49 49 56 98 98 102 125]
  ```

  And we get a flag! Albeit an encoded one.

6. It appears that this might be ASCII encoding ... as a quick check of an ASCII table

    112 = p
    105 = i
     99 = c
    111 = o

   So lets use CyberChef to do the translation for us....

   *picoCTF{b4d_brogrammer_******}*


4. Cut and paste the decoded flag into the picoCTF window to gain the credit



### Side Notes

1. We didn't need to provided *source* file after all
