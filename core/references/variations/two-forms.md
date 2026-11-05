# Variation: two-forms (products sold in more than one form)

Products: PT-141 (nasal spray · sublingual tablet), NAD+ (sublingual tablet · injection), GLP-1 (compounded semaglutide ·
compounded tirzepatide).

- **One form per ad.** The image question gains one item: "Form: pick per ad (Recommended) / <form A> / <form B>". "Pick per ad"
  alternates across the batch; the batch table shows the form per slot.
- The prompt attaches only that form's renders (`product.json` → `forms.<id>.bottle` / `.pill`); the other form never appears.
- Copy may name the form ("nasal spray", "sublingual tablet", "easy sublingual delivery"); never a strength, dose or count.
  Offers are per form where the bible says so (NAD+: tablet vs injection offers never mixed).
- Pill-focal slots go to the tablet form; bottle-focal slots to the spray / vial form; person slots either.
