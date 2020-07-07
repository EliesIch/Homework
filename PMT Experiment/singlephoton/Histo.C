{


TH1F h("h","Histogram",100,-0.1.,0.7.);

ifstream inp; double x;

inp.open("Result.csv");

while (inp >> x) { h.Fill(x); }

h.Draw();
inp.close();

}