import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("encoding_database.csv") #change file later

df.head()

y=df["Purchaswd"]
label_enc= LabelEncoder()
y_enc= label_enc.fit_transform(y)

y_enc
label_enc.inverse_transform(y_enc)

enc= OneHotEncoder()
enc_df= pd.DataFrame(enc.fit_transform(df[["Purchased"]]).toarray())

enc_df

enc= OneHotEncoder()
enc_df= pd.DataFrame(enc.fit_transform(df[["Color"]]).toarray())
enc_df