//[ Optical Broch 方程式の数値解を求める ]

//解く方程式
//{ dc_g/dt = -i(1/2) Ωge c_e exp(iδt)
//{ cc_e/dt = -i(1/2) Ω*ge c_g exp(-iδt)

//Rabi周波数
// Ωge = d_ge E*_L / ℏ

#include <iostream>
#include <fstream>
#include <complex>
#include <chrono>
#include <array>
#include <boost/numeric/odeint.hpp>
#include <boost/numeric/odeint/stepper/bulirsch_stoer.hpp>
#include <boost/numeric/odeint/stepper/bulirsch_stoer_dense_out.hpp>
//個人のパソコンで実行する場合はboostのライブラリはないので注意すること。

using namespace std;
using namespace boost::numeric::odeint;
typedef vector< complex <double> > state_type ;

//物理定数
const double hbar = 1.05451726e-34; //(h/2π)
const double PI2 = 2*M_PI;         //2π

// constants for the calculation
const double delta = 2*M_PI*0.0e6; //[rad/s]
const double dge = 1.0e-30;        //[C m]
const double EL = 1.0e4;           //[V/m]

// In order to measurement a caluculation time,
const auto startTime = std::chrono::system_clock::now();

//光学bloch方程式右辺
// x[0]: c_g
// x[1]: c_e
void twolevel(const state_type& x, state_type& dxdt, const double t)
{
  const complex <double> I(0.0, 1.0);
  dxdt[0] = -I/(2.*hbar) * x[1] * dge * EL * exp(I*delta*t);
  dxdt[1] = -I/(2.*hbar) * x[0] * dge * EL * exp(-I*delta*t);
}

struct streaming_observer
{
  std::ostream& m_out;
  streaming_observer( std::ostream &out ) : m_out( out ) { }

  template< class State >
  void operator() (const State &x , double t ) const
  {
    m_out << t;
    m_out << "\t" << x[0].real() << "\t" << x[0].imag();
    m_out << "\t" << x[1].real() << "\t" << x[1].imag();
    m_out << "\n";
  }
};


int main() {
    vector<double> timelog;
    vector< state_type > statelog;

    bulirsch_stoer< state_type > stepper( 1e-8 , 0.0 , 0.0 , 0.0 );

    //計算条件
    const double tstart = 0.0;
    const double tend = 25.0e-8;
    const double tstep = 1.0e-10;

    cout << "# Rabi freq: " << dge*EL/(hbar*PI2)*1e-6 << " [MHz]" << endl;

    //初期条件を代入
    state_type state0 = {
      complex<double>(1.0, 0.0),
      complex<double>(0.0, 0.0)
    };

    //微分方程式を解く

    integrate_const(stepper, twolevel, state0, tstart, tend, tstep , streaming_observer( cout ));

    //計算にかかった時間
    const auto odeEndTime = std::chrono::system_clock::now();

    const auto tOde = odeEndTime - startTime;
    cout << "# ODE:         ";
    cout << chrono::duration_cast<chrono::milliseconds>(tOde).count();
    cout << " [ms]" << endl;

    return 0;


}
