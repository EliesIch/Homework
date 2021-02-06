void his() {
  TH1F *source = new TH1F("source","source hist",100,-3,3);
  source->FillRandom("gaus",1000);
  TH1F *final = new TH1F("final","final hist",100,-3,3);

  // continued...

  for (Int_t i=0;i<10000;i++) {
    final->Fill(source->GetRandom());
  }
  TCanvas *c1 = new TCanvas("c1","c1",800,1000);
  c1->Divide(1,2);
  c1->cd(1);
  source->Draw();
  c1->cd(2);
  final->Draw();
  c1->cd();
}
