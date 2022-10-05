#!/usr/bin/env python3
# coding: utf8

# Homework 1
# We have encoded a text with a Caesar cypher
# Your job is to decode this cypher-ed text if our magic number is 3


SECRET = """
Zh*uh#qr#vwudqjhuv#wr#oryh
\rx#nqrz#wkh#uxohv#dqg#vr#gr#L#+gr#L,
D#ixoo#frpplwphqw*v#zkdw#L*p#wklqnlqj#ri
\rx#zrxogq*w#jhw#wklv#iurp#dq|#rwkhu#jx|

L#mxvw#zdqqd#whoo#|rx#krz#L*p#ihholqj
Jrwwd#pdnh#|rx#xqghuvwdqg

Qhyhu#jrqqd#jlyh#|rx#xs
Qhyhu#jrqqd#ohw#|rx#grzq
Qhyhu#jrqqd#uxq#durxqg#dqg#ghvhuw#|rx
Qhyhu#jrqqd#pdnh#|rx#fu|
Qhyhu#jrqqd#vd|#jrrge|h
Qhyhu#jrqqd#whoo#d#olh#dqg#kxuw#|rx

Zh*yh#nqrzq#hdfk#rwkhu#iru#vr#orqj
\rxu#khduw*v#ehhq#dfklqj/#exw#|rx*uh#wrr#vk|#wr#vd|#lw#+vd|#lw,
Lqvlgh/#zh#erwk#nqrz#zkdw*v#ehhq#jrlqj#rq#+jrlqj#rq,
Zh#nqrz#wkh#jdph#dqg#zh*uh#jrqqd#sod|#lw

Dqg#li#|rx#dvn#ph#krz#L*p#ihholqj
Grq*w#whoo#ph#|rx*uh#wrr#eolqg#wr#vhh

Qhyhu#jrqqd#jlyh#|rx#xs
Qhyhu#jrqqd#ohw#|rx#grzq
Qhyhu#jrqqd#uxq#durxqg#dqg#ghvhuw#|rx
Qhyhu#jrqqd#pdnh#|rx#fu|
Qhyhu#jrqqd#vd|#jrrge|h
Qhyhu#jrqqd#whoo#d#olh#dqg#kxuw#|rx

Qhyhu#jrqqd#jlyh#|rx#xs
Qhyhu#jrqqd#ohw#|rx#grzq
Qhyhu#jrqqd#uxq#durxqg#dqg#ghvhuw#|rx
Qhyhu#jrqqd#pdnh#|rx#fu|
Qhyhu#jrqqd#vd|#jrrge|h
Qhyhu#jrqqd#whoo#d#olh#dqg#kxuw#|rx

+Rrk/#jlyh#|rx#xs,
+Rrk/#jlyh#|rx#xs,
+Rrk,#Qhyhu#jrqqd#jlyh/#qhyhu#jrqqd#jlyh#+jlyh#|rx#xs,
+Rrk,#Qhyhu#jrqqd#jlyh/#qhyhu#jrqqd#jlyh#+jlyh#|rx#xs,

Zh*yh#nqrzq#hdfk#rwkhu#iru#vr#orqj
\rxu#khduw*v#ehhq#dfklqj/#exw#|rx*uh#wrr#vk|#wr#vd|#lw#+wr#vd|#lw,
Lqvlgh/#zh#erwk#nqrz#zkdw*v#ehhq#jrlqj#rq#+jrlqj#rq,
Zh#nqrz#wkh#jdph#dqg#zh*uh#jrqqd#sod|#lw

L#mxvw#zdqqd#whoo#|rx#krz#L*p#ihholqj
Jrwwd#pdnh#|rx#xqghuvwdqg

Qhyhu#jrqqd#jlyh#|rx#xs
Qhyhu#jrqqd#ohw#|rx#grzq
Qhyhu#jrqqd#uxq#durxqg#dqg#ghvhuw#|rx
Qhyhu#jrqqd#pdnh#|rx#fu|
Qhyhu#jrqqd#vd|#jrrge|h
Qhyhu#jrqqd#whoo#d#olh#dqg#kxuw#|rx

Qhyhu#jrqqd#jlyh#|rx#xs
Qhyhu#jrqqd#ohw#|rx#grzq
Qhyhu#jrqqd#uxq#durxqg#dqg#ghvhuw#|rx
Qhyhu#jrqqd#pdnh#|rx#fu|
Qhyhu#jrqqd#vd|#jrrge|h
Qhyhu#jrqqd#whoo#d#olh#dqg#kxuw#|rx

Qhyhu#jrqqd#jlyh#|rx#xs
Qhyhu#jrqqd#ohw#|rx#grzq
Qhyhu#jrqqd#uxq#durxqg#dqg#ghvhuw#|rx
Qhyhu#jrqqd#pdnh#|rx#fu|
Qhyhu#jrqqd#vd|#jrrge|h
Qhyhu#jrqqd#whoo#d#olh#dqg#kxuw#|rx
"""


def shift(t: str, n: int) -> str:
    i = ord(t)
    if i >= 127:
        raise ValueError("we only use the ascii table")

    return chr((i-n) % 128)


def decypher(t: str, n: int = 3) -> str:

    t = "".join([shift(x, n) for x in t])
    return t


def main():
    print(decypher(SECRET))


if __name__ == "__main__":
    main()
