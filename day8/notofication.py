from pushbullet import Pushbullet

pb = Pushbullet("o.KStpFExkqaYAtAGrQKJdBgASc2mFBvDe")
push = pb.push_note("testion", "OK")
print(push)