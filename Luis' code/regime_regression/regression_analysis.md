# Regime-Dependent Earnings Surprise Analysis

## 1. Regression Summary: What the Model Shows

### Model Specification

We estimate the following regression model:

\[
CAR_{i,t} =
\beta_0
+ \beta_1 \cdot Surprise_{i,t}
+ \beta_2 \cdot Regime_t
+ \beta_3 \cdot (Surprise_{i,t} \times Regime_t)
+ \varepsilon_{i,t}
\]

where:
- \( CAR_{i,t} \) is the cumulative abnormal return around firm \( i \)’s earnings announcement at time \( t \)
- \( Surprise_{i,t} \) is the earnings surprise
- \( Regime_t \) is a categorical macroeconomic regime indicator
- Robust (HC3) standard errors are used

This specification directly tests whether **the sensitivity of cumulative abnormal returns to earnings surprises varies across macroeconomic regimes**.

---

### Key Statistical Results (Plain English)

- The model explains approximately **4.6% of the variation in CAR**, which is **economically meaningful in an event-study context** where noise is high.
- The **baseline earnings surprise coefficient is statistically insignificant**, indicating that earnings surprises do not generate abnormal returns uniformly across all market conditions.
- The **interaction terms between earnings surprise and regime are positive**, implying that the market’s reaction to earnings surprises is **state-dependent rather than constant**.
- The strongest interaction effect is observed in **Regime 1 (Stress)**, with statistical significance at the 10% level and a large economic magnitude.

**Core takeaway:**  
> Earnings surprises matter, but only in certain macroeconomic environments.

---

## 2. Economic Interpretation by Regime

The regimes are defined as follows:

- **R0 – Calm**  
  Stable rates, low volatility, no flight to safety  
- **R1 – Stress**  
  VIX spikes, investors buy bonds, yields fall, heightened economic fear  
- **R2 – Tightening**  
  Central bank hiking rates, yields rising, little immediate market panic  

---

### R0 – Calm Regime

**Statistical result**
- Baseline surprise coefficient: negative and insignificant

**Economic interpretation**
In calm market conditions, earnings surprises do **not** generate systematic abnormal returns.

**Economic intuition**
- Information is largely anticipated
- Analyst forecasts are accurate
- Markets are liquid and efficient
- Firm-specific news is absorbed smoothly

**Translation**
> In stable environments, earnings announcements tend to confirm existing expectations rather than convey new information, resulting in limited abnormal price reactions.

---

### R1 – Stress Regime

**Statistical result**
- Surprise × Regime interaction is **large and positive**
- Marginal significance with strong economic magnitude

**Economic interpretation**
Earnings surprises have their **strongest impact on CAR during stress periods**.

**Economic intuition**
- Heightened uncertainty increases the value of firm-level fundamentals
- Investors reallocate capital aggressively
- Earnings announcements help distinguish resilient firms from vulnerable ones

**Translation**
> During periods of macroeconomic stress, earnings announcements become highly informative. Investors react more strongly to surprises as firm-level fundamentals matter more when the broader economic outlook is uncertain.

This represents the **central empirical finding** of the analysis.

---

### R2 – Tightening Regime

**Statistical result**
- Positive but smaller interaction effect
- Weaker statistical significance

**Economic interpretation**
Earnings surprises still influence returns, but the effect is **attenuated**.

**Economic intuition**
- Monetary policy dominates valuation
- Rising discount rates offset earnings news
- Macro policy signals compete with firm-level fundamentals

**Translation**
> In tightening cycles, earnings information is partially overshadowed by discount-rate effects, leading to weaker and less consistent abnormal returns.

---

## 3. Overall Economic Conclusion

The results indicate that:

> **The market’s processing of earnings information is regime-dependent. Earnings surprises are weakly priced in calm conditions, most strongly priced during periods of macroeconomic stress, and only moderately priced during monetary tightening cycles.**

This supports a macro-micro interaction view of asset pricing, where firm-level information is not priced uniformly across economic states.

---

## 4. Justification for Regime Construction

### Why Use Regime Classification?

Financial markets do not operate in a single continuous state. Instead, investor behaviour, risk tolerance, and information processing vary across distinct macroeconomic environments. Regime-based analysis allows these non-linear dynamics to be captured more effectively than continuous controls alone.

---

### Role of VIX

- VIX measures expected equity market volatility
- Serves as a proxy for:
  - risk aversion
  - uncertainty
  - demand for safe assets
- Spikes during crises, recessions, and stress events

**Why it matters**
> VIX captures the psychological and risk-based state of the market, which strongly influences how new information is processed by investors.

---

### Role of 3-Month Percentage Change in 10-Year Treasury Yield (DSG10)

- Captures medium-term shifts in long-term interest rates
- Reflects:
  - monetary tightening vs easing
  - growth expectations
  - inflation outlook
- Changes are more informative than levels because they capture **direction and momentum**

**Why a 3-month horizon**
- Smooths high-frequency noise
- Aligns with macro policy cycles
- Captures sustained regime transitions rather than transitory shocks

---

### Why the Combination Works

| Variable | Captures |
|-------|---------|
| VIX | Risk sentiment and uncertainty |
| 3-month % Δ DSG10 | Policy stance and growth expectations |

Together, these measures allow regimes to distinguish between:
- calm growth environments
- tightening cycles without fear
- stress-driven flight-to-safety periods

**Methodological justification**
> Combining volatility-based and yield-based measures enables regime classification to reflect both investor sentiment and macroeconomic fundamentals, providing a comprehensive representation of the economic environment faced by market participants.

---

## 5. Final Positioning

This approach is:
- Economically motivated
- Methodologically consistent
- Aligned with macro-finance literature
- Directly tied to the research question

The analysis provides a coherent explanation of **when and why earnings surprises matter**, rather than whether they matter on average.
