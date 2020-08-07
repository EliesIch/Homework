
{ 
    gStyle->SetOptFit(112);
    //TFile *f = new TFile("basic.root"); 

    //f->ls(); 
    TH1F h1("h1","Test;Area;Events",80,-50,500);
   
    ifstream inp; double x;

    inp.open("test.csv");

    while (inp >> x) { h1.Fill(x); }
   
    //h1.Fit("gaus"); 
    /*Double_t par[9];
    TF1 *g1    = new TF1("g1","gaus",-0.1,0.05);
    TF1 *g2    = new TF1("g2","gaus",0.05,0.2);
    TF1 *g3    = new TF1("g3","gaus",0.2,0.8);
    TF1 *total = new TF1("total","gaus(0)+gaus(3)+gaus(6)",-0.1,1);
    total->SetLineColor(2);
    h1.Fit(g1,"R");
    h1.Fit(g2,"R+");
    h1.Fit(g3,"R+");
    g1->GetParameters(&par[0]);
    g2->GetParameters(&par[3]);
    g3->GetParameters(&par[6]);
    total->SetParameters(par);
    h1.Fit(total,"R+");*/

    h1.Draw(); 
    
}




