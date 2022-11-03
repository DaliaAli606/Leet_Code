{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "    def longestPalindrome(self, words: List[str]) -> int:\n",
    "        # a count variable contains the number of occurrences of each word\n",
    "        count = Counter(words)  # count the count of word occurrences in a list \n",
    "        answer = 0  #denote the number of words in the final string\n",
    "        central = False  # denote whether we have a central word\n",
    "        for word, count_of_the_word in count.items():\n",
    "            # if the word is a palindrome\n",
    "            if word[0] == word[1]:  # if they are equal \n",
    "                if count_of_the_word % 2 == 0:  # see the reminder is zero then teh divition is even \n",
    "                    answer += count_of_the_word  # add the value to the answer varable \n",
    "                else:\n",
    "                    answer += count_of_the_word - 1   # else , remove from answer and add to central\n",
    "                    central = True # this can be considered as ascentral number \n",
    "            # consider a pair of non-palindrome words,\n",
    "            # such that one is the reverse of another\n",
    "            # word[1] + word[0] is the reversed word\n",
    "            elif word[0] < word[1]:\n",
    "                answer += 2 * min(count_of_the_word, count[word[1] + word[0]])\n",
    "        if central:\n",
    "            answer += 1\n",
    "        return 2 * answer  #Because each word has a length of 22"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "e6bdcef1271a5e02e8a579499f4634537e7900e40c2944de6a7dc2628543d20c"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
