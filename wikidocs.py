from pandas import Series, DataFrame

data = {"open": [737, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]} 
df = DataFrame(data) 
s = Series([300, 400])  #DataFrame에 추가할 Series 객체를 생성
df["volume"] = s        #DataFrame에 volume이란 이름으로 Series 객체를 추가
print(df)
df.loc[2] = (100, 200, 300, 400, 500)   #행을 추가할 때는 loc를 사용해서 행의 이름과 데이터를 튜플 혹은 리스트로 넘겨주면 됩
print(df)
upper = df["open"] * 1.3
df["upper"] = upper
print(df)