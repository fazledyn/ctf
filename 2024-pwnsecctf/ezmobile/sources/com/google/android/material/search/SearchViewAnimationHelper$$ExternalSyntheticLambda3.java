package com.google.android.material.search;

import android.animation.ValueAnimator;
import com.google.android.material.internal.FadeThroughDrawable;

/* compiled from: D8$$SyntheticClass */
public final /* synthetic */ class SearchViewAnimationHelper$$ExternalSyntheticLambda3 implements ValueAnimator.AnimatorUpdateListener {
    public final /* synthetic */ FadeThroughDrawable f$0;

    public /* synthetic */ SearchViewAnimationHelper$$ExternalSyntheticLambda3(FadeThroughDrawable fadeThroughDrawable) {
        this.f$0 = fadeThroughDrawable;
    }

    public final void onAnimationUpdate(ValueAnimator valueAnimator) {
        this.f$0.setProgress(((Float) valueAnimator.getAnimatedValue()).floatValue());
    }
}
