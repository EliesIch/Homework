void c()
{
//=========Macro generated from canvas: c/XY plot
//=========  (Sun Aug  2 13:08:58 2020) by ROOT version 6.20/04
   TCanvas *c = new TCanvas("c", "XY plot",0,23,1536,803);
   c->Range(-7.5,-8.75,7.5,28.75);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetFrameLineColor(0);
   c->SetFrameBorderMode(0);
   c->SetFrameLineColor(0);
   c->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1[11] = {
   -5,
   -4,
   -3,
   -2,
   -1,
   0,
   1,
   2,
   3,
   4,
   5};
   Double_t Graph0_fy1[11] = {
   25,
   16,
   9,
   4,
   1,
   0,
   1,
   4,
   9,
   16,
   25};
   TGraph *graph = new TGraph(11,Graph0_fx1,Graph0_fy1);
   graph->SetName("Graph0");
   graph->SetTitle("E_{k} = #frac{#hbar^{2}k^{2}}{2m}");
   graph->SetFillStyle(1000);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ff0000");
   graph->SetLineColor(ci);
   graph->SetMarkerStyle(3);
   
   TH1F *Graph_Graph01 = new TH1F("Graph_Graph01","E_{k} = #frac{#hbar^{2}k^{2}}{2m}",100,-6,6);
   Graph_Graph01->SetMinimum(-5);
   Graph_Graph01->SetMaximum(25);
   Graph_Graph01->SetDirectory(0);
   Graph_Graph01->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph01->SetLineColor(ci);
   Graph_Graph01->GetXaxis()->SetAxisColor(0);
   Graph_Graph01->GetXaxis()->SetLabelFont(42);
   Graph_Graph01->GetXaxis()->SetLabelSize(0);
   Graph_Graph01->GetXaxis()->SetTickLength(0);
   Graph_Graph01->GetXaxis()->SetTitleOffset(1);
   Graph_Graph01->GetXaxis()->SetTitleFont(42);
   Graph_Graph01->GetYaxis()->SetAxisColor(0);
   Graph_Graph01->GetYaxis()->SetLabelFont(42);
   Graph_Graph01->GetYaxis()->SetLabelSize(0);
   Graph_Graph01->GetYaxis()->SetTickLength(0);
   Graph_Graph01->GetYaxis()->SetTitleFont(42);
   Graph_Graph01->GetZaxis()->SetLabelFont(42);
   Graph_Graph01->GetZaxis()->SetTitleOffset(1);
   Graph_Graph01->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph01);
   
   
   TF1 *PrevFitTMP2 = new TF1("PrevFitTMP","pol2",-6,6, TF1::EAddToList::kNo);
   PrevFitTMP2->SetFillColor(19);
   PrevFitTMP2->SetFillStyle(0);
   PrevFitTMP2->SetLineColor(2);
   PrevFitTMP2->SetLineWidth(2);
   PrevFitTMP2->GetXaxis()->SetLabelFont(42);
   PrevFitTMP2->GetXaxis()->SetTitleOffset(1);
   PrevFitTMP2->GetXaxis()->SetTitleFont(42);
   PrevFitTMP2->GetYaxis()->SetLabelFont(42);
   PrevFitTMP2->GetYaxis()->SetTitleFont(42);
   PrevFitTMP2->SetParameter(0,0);
   PrevFitTMP2->SetParError(0,0.4554769);
   PrevFitTMP2->SetParLimits(0,0,0);
   PrevFitTMP2->SetParameter(1,0);
   PrevFitTMP2->SetParError(1,0.09534626);
   PrevFitTMP2->SetParLimits(1,0,0);
   PrevFitTMP2->SetParameter(2,1);
   PrevFitTMP2->SetParError(2,0.03413944);
   PrevFitTMP2->SetParLimits(2,0,0);
   PrevFitTMP2->SetParent(graph);
   graph->GetListOfFunctions()->Add(PrevFitTMP2);
   graph->Draw("AP");
   
   TPaveText *pt = new TPaveText(0.5759452,0.8406452,0.7408735,0.9606452,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("E_{k} = #frac{#hbar^{2}k^{2}}{2m}");
   pt->Draw();
   TGaxis *gaxis = new TGaxis(0,-5,0,25,-5,25,6,"G");
   gaxis->SetLabelOffset(0.005);
   gaxis->SetLabelSize(0.04);
   gaxis->SetTickSize(0.03);
   gaxis->SetGridLength(0);
   gaxis->SetTitleOffset(1);
   gaxis->SetTitleSize(0.04);
   gaxis->SetTitleColor(1);
   gaxis->SetTitleFont(62);
   gaxis->Draw();
   TLatex *   tex = new TLatex(-0.5,25,"E_{k}");
   tex->SetTextAlign(31);
   tex->SetLineWidth(2);
   tex->Draw();
   gaxis = new TGaxis(-6,0,6,0,-6,6,510,"G");
   gaxis->SetLabelOffset(0.005);
   gaxis->SetLabelSize(0.04);
   gaxis->SetTickSize(0.03);
   gaxis->SetGridLength(0);
   gaxis->SetTitleOffset(1);
   gaxis->SetTitleSize(0.04);
   gaxis->SetTitleColor(1);
   gaxis->SetTitleFont(62);
   gaxis->Draw();
      tex = new TLatex(6,-2,"#mbox{k}");
   tex->SetTextAlign(31);
   tex->SetLineWidth(2);
   tex->Draw();
   TArrow *arrow = new TArrow(0,24,0,25,0.02,"|>");
   arrow->SetFillColor(1);
   arrow->SetFillStyle(1001);
   arrow->SetLineWidth(2);
   arrow->SetAngle(40);
   arrow->Draw();
   arrow = new TArrow(5.9,0,6,0,0.02,"|>");
   arrow->SetFillColor(1);
   arrow->SetFillStyle(1001);
   arrow->SetLineWidth(2);
   arrow->SetAngle(40);
   arrow->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
