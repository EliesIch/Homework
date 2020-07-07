
{ 
    TFile *f = new TFile("basic.root"); 

    f->ls(); 


    TH1F * h1 = (TH1F*)f->Get("h1"); 

    h1->Draw(); 

}




