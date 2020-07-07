#include "TString.h"
#include "TSystem.h"
#include "TInterpreter.h"
#include "TFile.h"
#include "TNtuple.h"
#include "TH1.h"

#include <fstream>
#include <cstdio>

void basic(const char *file_in = "Result01.txt",
           const char *file_out = "basic.root")
{
  if ((!file_in) || (!(file_in[0]))) return; // just a precaution
  if ((!file_out) || (!(file_out[0]))) return; // just a precaution
  
  ifstream in;
  
#if 1 /* 0 or 1 */
  // ... from the current subdirectory ...
  in.open(file_in);
#else /* 0 or 1 */
  // ... from the subdirectory where the "basic.C" macro is located ...
  TString dir = gSystem->UnixPathName(gInterpreter->GetCurrentMacroName());
  dir.ReplaceAll("basic.C", "");
  dir.ReplaceAll("/./", "/");
  in.open(Form("%s%s", dir.Data(), file_in));
#endif /* 0 or 1 */
  
  Float_t x;
  Int_t nlines = 0;
  TFile *f = new TFile(file_out, "RECREATE");
  TNtuple *ntuple = new TNtuple("ntuple", "data from ascii file", "x");
  
  while (1) {
    in >> x;
    if (in.fail()) break;
    // if (!in.good()) break; // needs a "newline" character at the end
    if (nlines < 5) printf("x=%11f\n", x);
    ntuple->Fill(x);
    nlines++;
  }
  printf(" found %d points\n", nlines);
  
  in.close();
  
  Int_t xbins = 100;
  Double_t xmin = ntuple->GetMinimum("x");
  Double_t xmax = ntuple->GetMaximum("x");
  xmax += ((xmax - xmin) / xbins ) * 0.001; // make it "slightly higher"
  // xmax += ((xmax - xmin) / xbins ) / xbins; // make it "slightly higher"
  TH1F *h1 = new TH1F("h1", "x distribution", xbins, xmin, xmax);
  
#if 1 /* 0 or 1 */
  ntuple->Project("h1", "x");
#else /* 0 or 1 */
  ntuple->Draw("x >> h1", "", "goff");
#endif /* 0 or 1 */
  
  f->Write();
}
