package com.venu.practive.assignments.assignment1;

public class MiddleWord {

    public static void main(String[] args) {
        MiddleWord mw = new MiddleWord();
        String a = mw.find("god");
        System.out.println(" Middle word for god is " + a);

        String b = mw.find("good");
        System.out.println(" Middle word for good is " + b);

        String c = mw.find("jack low");
        System.out.println(" Middle word for jack low is " + c);

    }


    /**
     * This should find the middle word of the given word
     * If the word is dog then it should return o
     * if the word is food then it should return oo
     * @param a
     * @return
     */

    private String find(String a) {
        return "";
    }

}
