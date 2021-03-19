void xyplot ()
{
   TCanvas *c = new TCanvas("c","XY plot",200,10,700,500);

   // Remove the frame
   c->SetFillColor(kWhite);
   c->SetFrameLineColor(kWhite);
   c->SetFrameBorderMode(0);

   const Int_t n = 11;
   Double_t x[n] = {-5,-4,-3,-2,-1,0,1,2,3,4,5};
   Double_t y[n] = {25,16,9,4,1,0,1,4,9,16,25};
   TGraph *gr = new TGraph(n,x,y);
   gr->SetTitle("E_{k} = #frac{#hbar^{2}k^{2}}{2m}");
   gr->SetMinimum(-5);
   gr->SetMaximum(25);
   gr->SetLineColor(kRed);
   gr->Draw("AP*");

   // Remove the frame's axis
   gr->GetHistogram()->GetYaxis()->SetTickLength(0);
   gr->GetHistogram()->GetXaxis()->SetTickLength(0);
   gr->GetHistogram()->GetYaxis()->SetLabelSize(0);
   gr->GetHistogram()->GetXaxis()->SetLabelSize(0);
   gr->GetHistogram()->GetXaxis()->SetAxisColor(0);
   gr->GetHistogram()->GetYaxis()->SetAxisColor(0);

   gPad->Update();

   // Draw orthogonal axis system entered at (0,0)
   TGaxis *yaxis = new TGaxis(0, gPad->GetUymin(),
                              0, gPad->GetUymax(),
                              gPad->GetUymin(),gPad->GetUymax(),6,"G");
   yaxis->Draw();
   TLatex *ytitle = new TLatex(-0.5,gPad->GetUymax(),"E_{k}");
   ytitle->Draw();
   ytitle->SetTextSize(0.05);
   ytitle->SetTextAngle(0.);
   ytitle->SetTextAlign(31);
   TGaxis *xaxis = new TGaxis(gPad->GetUxmin(), 0,
                              gPad->GetUxmax(), 0,
                              gPad->GetUxmin(),gPad->GetUxmax(),510,"G");
   xaxis->Draw();
   TLatex *xtitle = new TLatex(gPad->GetUxmax(),-2,"#mbox{k}");
   xtitle->Draw();
   xtitle->SetTextAlign(31);
   xtitle->SetTextSize(0.05);
   TArrow *ar2 = new TArrow(0,24,0,25,0.02,"|>");
   ar2->SetAngle(40);
   ar2->SetLineWidth(2);
   ar2->Draw();
   TArrow *ar1 = new TArrow(5.9,0,6,0,0.02,"|>");
   ar1->SetAngle(40);
   ar1->SetLineWidth(2);
   ar1->Draw();
}