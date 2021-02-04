{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "capital-banking",
   "metadata": {},
   "outputs": [],
   "source": [
    "def quicksort(alist, start, end):\n",
    "    '''Sorts the list from indexes start to end - 1 inclusive.'''\n",
    "    if end - start > 1:\n",
    "        p = partition(alist, start, end)\n",
    "        quicksort(alist, start, p)\n",
    "        quicksort(alist, p + 1, end)\n",
    " \n",
    " \n",
    "def partition(alist, start, end):\n",
    "    pivot = alist[start]\n",
    "    i = start + 1\n",
    "    j = end - 1\n",
    " \n",
    "    while True:\n",
    "        while (i <= j and alist[i] <= pivot):\n",
    "            i = i + 1\n",
    "        while (i <= j and alist[j] >= pivot):\n",
    "            j = j - 1\n",
    " \n",
    "        if i <= j:\n",
    "            alist[i], alist[j] = alist[j], alist[i]\n",
    "        else:\n",
    "            alist[start], alist[j] = alist[j], alist[start]\n",
    "            return j\n",
    " \n",
    " \n",
    "alist = input('Enter the list of numbers: ').split()\n",
    "alist = [int(x) for x in alist]\n",
    "quicksort(alist, 0, len(alist))\n",
    "print('Sorted list: ', end='')\n",
    "print(alist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "improving-waste",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
